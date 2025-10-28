import argparse
from main import mcp

def main():
    """MCP Wiki: Read Asset Repo."""
    parser = argparse.ArgumentParser(
        description="Gives you the ability to read Asset "
    )
    parser.parse_args()
    mcp.run()

if __name__ == "__main__":
    main()