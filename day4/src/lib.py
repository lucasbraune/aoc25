from pathlib import Path

INPUT = Path(__file__).resolve().parent.parent / "resources" / "input.txt"


def read_input() -> str:
    return INPUT.read_text()


def to_matrix(input: str) -> list[list[str]]:
    return [list(line) for line in input.splitlines()]


def increment_adjacent(counts: list[list[int]], *, i: int, j: int) -> None:
    rows = len(counts)
    cols = len(counts[0])
    for delta_i in [-1, 0, 1]:
        if i + delta_i < 0 or i + delta_i >= rows:
            continue
        for delta_j in [-1, 0, 1]:
            if j + delta_j < 0 or j + delta_j >= cols:
                continue
            if delta_j == 0 and delta_i == 0:
                continue
            counts[i + delta_i][j + delta_j] += 1


def adjacent_counts(diagram: list[list[str]]) -> list[list[int]]:
    rows = len(diagram)
    cols = len(diagram[0])
    counts = [[0] * cols for _ in range(rows)]
    for i in range(0, rows):
        for j in range(0, cols):
            if diagram[i][j] == "@":
                increment_adjacent(counts, i=i, j=j)
    return counts


def count_removed(diagram: list[list[str]]):
    count = 0
    for row in diagram:
        for c in row:
            if c == "x":
                count += 1
    return count


def remove(diagram: list[list[str]]) -> int:
    rows = len(diagram)
    cols = len(diagram[0])
    removed_before = count_removed(diagram)

    counts = adjacent_counts(diagram)
    for i in range(rows):
        for j in range(cols):
            if diagram[i][j] == "@" and counts[i][j] < 4:
                diagram[i][j] = "x"

    removed_after = count_removed(diagram)
    return removed_after - removed_before
