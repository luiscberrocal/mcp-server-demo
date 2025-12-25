"""
FastMCP quickstart example.

Run from the repository root:
    uv run examples/snippets/servers/fastmcp_quickstart.py
"""
from pathlib import Path

from mcp.server.fastmcp import FastMCP

NOTES_FOLDER = Path(__file__).parent / "output" / "notes"
NOTES_FILE = NOTES_FOLDER / "notes.txt"

def ensure_file():
    """Ensure the notes file exists."""
    NOTES_FOLDER.mkdir(parents=True, exist_ok=True)
    if not NOTES_FILE.exists():
        with open(NOTES_FILE, "w", encoding="utf-8") as f:
            f.write("")

# Create an MCP server
mcp = FastMCP("AI Sticky Notes", json_response=True)

@mcp.tool()
def add_note(message:str) -> str:
    """Append a new note to a sticky note file.

    Args:
        message (str): The message to add.
    Returns:
        str: Confirmation message that the note was saved.
    """
    ensure_file()
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")
    return "Note added."

@mcp.tool()
def read_notes() -> str:
    """Read all sticky notes from the file.

    Returns:
        str: All notes concatenated into a single string.
    """
    ensure_file()
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        content = f.read().strip()
    return content if content else "No notes found."

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """Get the latest sticky note.

    Returns:
        str: The latest note or a message if no notes exist.
    """
    ensure_file()
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if lines:
        return lines[-1].strip()
    return "No notes found."

@mcp.prompt()
def notes_summary_prompt() -> str:
    """Generate a prompt asking AI to summarize all sticky notes.

    Returns:
        str: A prompt string for summarizing notes.
    """
    notes = read_notes()
    if not notes:
        return "No notes found."
    return f"Summarize the following sticky notes:\n{notes}"