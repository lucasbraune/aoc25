from pathlib import Path

INPUT = Path(__file__).resolve().parent.parent / "resources" / "input.txt"


def read_input() -> str:
    return INPUT.read_text()


def parse_diagram(diagram_str: str) -> list[list[str]]:
    return [list(line) for line in diagram_str.splitlines()]


def render_diagram(diagram: list[list[str]]) -> str:
    return "\n".join("".join(row) for row in diagram)


