# calendar-mcp

An MCP server built with [FastMCP](https://gofastmcp.com) that lets Claude manage calendar events through natural language. Add, view, and delete events — all stored locally in a custom format.

Built as a first FastMCP project following the [Codecademy MCP Server tutorial](https://www.codecademy.com/article/build-an-mcp-server).

---

## Features

- **Add events** — create events with a title, date, and description
- **View events** — list all upcoming events
- **Delete events** — remove events by title or date
- **Custom local storage** — events persisted to a local file in a custom format
- **Claude Desktop integration** — works via stdio transport

---

## Tech Stack

- [FastMCP](https://gofastmcp.com) — Python MCP server framework
- [uv](https://docs.astral.sh/uv/) — project and dependency management
- Claude Desktop — MCP client

---

## Getting Started

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) installed
- Claude Desktop installed

### Installation

```bash
git clone https://github.com/cubaseuser123/calendar-mcp
cd calendar-mcp
uv sync
```

### Connect to Claude Desktop

Add the following to your Claude Desktop config file:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "calendar-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/calendar-mcp",
        "run",
        "main.py"
      ]
    }
  }
}
```

Restart Claude Desktop. You should see the calendar-mcp tools available in the tools menu.

---

## Usage

Once connected, you can talk to Claude naturally:

> "Add an event called Team Standup on March 20th at 10am"

> "What events do I have coming up?"

> "Delete the Team Standup event"

---

## Project Structure

```
calendar-mcp/
├── main.py          # FastMCP server + tool definitions
├── storage.py       # Custom local storage logic
├── events.json      # Auto-generated event store
├── pyproject.toml   # uv project config
└── README.md
```

---

## What I Learned

- Setting up a FastMCP server with `uv` and `pyproject.toml`
- Registering tools using the `@mcp.tool` decorator
- Connecting a local MCP server to Claude Desktop via stdio
- Designing a simple custom storage format for persistence

---

## Next Steps

This is Project 1 in a series of FastMCP learning projects:

- ✅ **Project 1** — calendar-mcp (this repo)
- 🔜 **Project 2** — Document parser MCP with resources, MCP Inspector, and PyPI packaging

---

## Resources

- [FastMCP Docs](https://gofastmcp.com)
- [Codecademy Tutorial](https://www.codecademy.com/article/build-an-mcp-server)
- [MCP Protocol Docs](https://modelcontextprotocol.io)
