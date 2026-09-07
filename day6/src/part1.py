import lib
from lib import Problem


def parse_problems(s: str) -> list[Problem]:
    lines = s.splitlines()
    operands = [[int(x) for x in line.split()] for line in lines[:-1]]
    operators: list[lib.Operator] = [
        lib.ensure_operator(op) for op in lines[-1].split()
    ]
    return [
        Problem([operand[problem] for operand in operands], operators[problem])
        for problem in range(len(operators))
    ]


def solve() -> int:
    s = lib.read_input()
    return lib.grand_total(parse_problems(s))


if __name__ == "__main__":
    print(solve())
