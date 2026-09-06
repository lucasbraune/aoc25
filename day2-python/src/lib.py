from dataclasses import dataclass
from pathlib import Path

INPUT = Path(__file__).resolve().parent.parent / "resources" / "input.txt"


def read_input() -> str:
    return INPUT.read_text()


@dataclass(frozen=True)
class Range:
    start: int
    end: int

    def __post_init__(self):
        if self.start >= self.end:
            raise ValueError(f"start must be < end, got {self.start} >= {self.end}")


def parse_range(range_str: str) -> Range:
    start, end = range_str.split("-")
    return Range(int(start), int(end))


def parse_input(input: str) -> list[Range]:
    list_str = input.splitlines()[0]
    return [parse_range(item) for item in list_str.split(",")]
