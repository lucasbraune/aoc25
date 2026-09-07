from collections.abc import Sequence

import lib


def transpose(input: Sequence[str]) -> list[str]:
    rows = len(input)
    cols = len(input[0])
    result: list[str] = []
    for j in range(cols):
        result_row = []
        for i in range(rows):
            result_row.append(input[i][j])
        result.append("".join(result_row))
    return result


def parse_problems(input: str) -> list[lib.Problem]:
    problems = []
    # input_t.pop() outputs the columns of `input` in order
    input_t = transpose(input.splitlines())[::-1]
    while input_t:
        first_line = input_t.pop()
        operator = lib.ensure_operator(first_line[-1])
        operands = [int(first_line[:-1])]
        while line := (input_t.pop().strip() if input_t else None):
            operands.append(int(line))
        problems.append(lib.Problem(operands, operator))
    return problems


def grand_total(input: str) -> int:
    problems = parse_problems(input)
    return sum(lib.evaluate(p.operator, p.operands) for p in problems)


def solve() -> int:
    return grand_total(lib.read_input())


if __name__ == "__main__":
    print(solve())
