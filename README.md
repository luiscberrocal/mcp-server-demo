# MCP Server Demo


This repository contains a demo implementation of an MCP (Model Context Protocol) server using the MCP Python library. 
The server is designed to interact with Claude Desktop, providing a seamless experience for users.

This is based on :

- [Youtube Video by Tech with Tim](https://youtu.be/-8k9lGpGQ6g?si=ZQqb2OfK7i7Sg4MQ).
- [MCP Avanded Server Example](https://youtu.be/j5f2EQf5hkw?si=dkX2-3fVyAveyoyW) The code does not work.
- [MCP Crash Course](https://youtu.be/5xqFjh56AwM?si=LPJGlTsD4ECGA0dO)
  - [GitHub Repository](https://github.com/daveebbelaar/ai-cookbook/tree/main/mcp/crash-course)



```shell
 uv run mcp dev server.py   
```



## Configuration

### Install Claude Desktop


### Copy Configuration File

```shell
cp ./configurations/claude_desktop_config.json ~/.config/Claude     
```

## Resources

- [MCP Python Library](https://github.com/modelcontextprotocol/python-sdk)