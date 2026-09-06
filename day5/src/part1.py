import lib
from lib import Input


def fresh_ingredients(input: Input) -> list[int]:
    return [x for x in input.available if any(r.contains(x) for r in input.ranges)]


def solve() -> int:
    input = lib.parse_input(lib.read_input())
    return len(fresh_ingredients(input))


if __name__ == "__main__":
    print(solve())
