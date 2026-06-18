
def main():
    print("Hello from mcp-with-client!")


if __name__ == "__main__":
    main()

from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Code Explorer")

@mcp.tool()
def list_files(directory: str = ".") -> list[str]:
    """List files in a directory."""
    path = Path(directory)

    if not path.exists():
        return ["Directory not found"]

    return [str(f) for f in path.iterdir()]

@mcp.tool()
def read_file(filepath: str) -> str:
    """Read contents of a file."""

    path = Path(filepath)

    if not path.exists():
        return "File not found"

    return path.read_text()

@mcp.tool()
def count_lines(filepath: str) -> int:
    """Count lines in a file."""

    path = Path(filepath)

    if not path.exists():
        return -1

    return len(path.read_text().splitlines())

if __name__ == "__main__":
    mcp.run()
    

