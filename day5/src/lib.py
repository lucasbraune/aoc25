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
        if self.start > self.end:
            raise ValueError(f"Start must be <= end, got {self.start} > {self.end}")

    def contains(self, value: int) -> bool:
        return value >= self.start and value <= self.end

    def cardinality(self) -> int:
        return self.end - self.start + 1


@dataclass(frozen=True)
class Input:
    ranges: list[Range]
    available: list[int]


def parse_range(raw: str) -> Range:
    start, end = raw.split("-")
    return Range(int(start), int(end))


def parse_input(raw: str) -> Input:
    blank_line_seen = False
    ranges = []
    available = []
    for line in raw.splitlines():
        if not line:
            blank_line_seen = True
            continue
        if not blank_line_seen:
            ranges.append(parse_range(line))
        else:
            available.append(int(line))
    return Input(ranges, available)
