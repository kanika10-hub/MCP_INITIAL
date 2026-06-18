from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Code Explorer")

@mcp.tool()
def read_file(filepath: str) -> str:
    """Read a file and return its contents."""

    path = Path(filepath)

    if not path.exists():
        return "File not found"

    return path.read_text(encoding="utf-8")

@mcp.tool()
def list_files(directory: str = ".") -> list[str]:
    """List files in a directory."""

    return [str(f) for f in Path(directory).iterdir()]




if __name__ == "__main__":
    print("Starting Code Explorer MCP server...")
    mcp.run()