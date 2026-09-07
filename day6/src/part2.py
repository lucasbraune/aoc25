from collections.abc import Sequence
from itertools import groupby

import lib


def transpose(rows: Sequence[str]) -> list[str]:
    return ["".join(col) for col in zip(*rows, strict=True)]


def parse_problems(s: str) -> list[lib.Problem]:
    # Each problem is a run of columns, separated by all-blank columns. Its
    # operands are written vertically, and its operator sits at the bottom of
    # the first column.
    columns = transpose(s.splitlines())
    problems: list[lib.Problem] = []
    for blank, group in groupby(columns, key=lambda col: not col.strip()):
        if blank:
            continue
        first, *rest = group
        operands = [int(first[:-1]), *(int(col) for col in rest)]
        problems.append(lib.Problem(operands, lib.ensure_operator(first[-1])))
    return problems


def solve() -> int:
    return lib.grand_total(parse_problems(lib.read_input()))


if __name__ == "__main__":
    print(solve())
