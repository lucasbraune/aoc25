import lib
from lib import Problem


def parse_problems(s: str) -> list[Problem]:
    grid = [line.split() for line in s.splitlines()]
    # Transposing puts one whole problem on each row: operands, then operator.
    grid_transpose = zip(*grid, strict=True)
    return [
        Problem([int(x) for x in operands], lib.ensure_operator(operator))
        for *operands, operator in grid_transpose
    ]


def solve() -> int:
    return lib.grand_total(parse_problems(lib.read_input()))


if __name__ == "__main__":
    print(solve())
