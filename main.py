import os

from fastmcp import FastMCP
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from fastmcp.server.auth import BearerAuthProvider

load_dotenv()

auth = BearerAuthProvider(
    jwks_uri=f"{os.getenv('STITCH_DOMAIN')}/.well-known/jwks.json",
    issuer=os.getenv("STITCH_DOMAIN"),
    algorithm="RS256",
    audience=os.getenv("STITCH_PROJECT_ID")
)

mcp = FastMCP(name="Notes App")


@mcp.tool()
def get_user_notes(user_id: str) -> str:
    """Get all notes for a specific user.

    Args:
        user_id (str): The ID of the user.
    """
    return f"No notes found for user {user_id}"


@mcp.tool()
def add_note(content: str, user_id: str) -> str:
    """Add a note for a specific user.

    Args:
        content (str): The content of the note.
        user_id (str): The ID of the user.
    """
    return f"Note added for user {user_id}: {content}"


if __name__ == '__main__':
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=8000,
        middleware=[
            Middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )
        ]
    )
