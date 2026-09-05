from pathlib import Path

from lib import total_output


def solve() -> int:
    path = Path(".").parent / "resources" / "input.txt"
    with open(path) as file:
        return total_output(file.read(), batteries=12)


if __name__ == "__main__":
    print(solve())
