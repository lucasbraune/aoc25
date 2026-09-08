import lib


def evolve(diagram: list[list[str]]) -> None:
    rows = len(diagram)
    cols = len(diagram[0])
    for i in range(1, rows):
        curr = diagram[i]
        prev = diagram[i - 1]
        for j in range(cols):
            empty_space = curr[j] == "."
            incoming_beam = prev[j] == "|" or prev[j] == "S"
            left_branch = j + 1 < cols and curr[j + 1] == "^" and prev[j + 1] == "|"
            right_branch = j - 1 >= 0 and curr[j - 1] == "^" and prev[j - 1] == "|"
            if empty_space and (incoming_beam or left_branch or right_branch):
                curr[j] = "|"


def count_splits(diagram_str: str) -> int:
    diagram = lib.parse_diagram(diagram_str)
    rows = len(diagram)
    cols = len(diagram[0])
    evolve(diagram)
    splits = 0
    for i in range(1, rows):
        curr = diagram[i]
        prev = diagram[i - 1]
        for j in range(cols):
            if curr[j] == "^" and prev[j] == "|":
                splits += 1
    return splits


def solve() -> int:
    return count_splits(lib.read_input())


if __name__ == "__main__":
    print(solve())
