from pathlib import Path

INPUT = Path(__file__).resolve().parent.parent / "resources" / "input.txt"


def read_input() -> str:
    return INPUT.read_text()
