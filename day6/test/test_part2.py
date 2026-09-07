import lib
import part2


def test_grand_total(example: str) -> None:
    assert lib.grand_total(part2.parse_problems(example)) == 3263827


def test_solve() -> None:
    assert part2.solve() == 9876636978528
