import lib
import part1


def test_grand_total(example: str) -> None:
    assert lib.grand_total(part1.parse_problems(example)) == 4277556


def test_solve() -> None:
    assert part1.solve() == 5322004718681
