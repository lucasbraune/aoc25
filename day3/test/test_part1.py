import pytest

import part1


def test_argmax():
    arr = [1, 3, 2]
    assert part1.argmax(arr) == 1


@pytest.mark.parametrize(
    "bank, expected",
    [
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
    ],
)
def test_jolage(bank: str, expected: int):
    assert part1.joltage(bank) == expected


def test_total_output():
    banks = """
    987654321111111
    811111111111119
    234234234234278
    818181911112111
    """
    print(banks)
    assert part1.total_output(banks) == 357


def test_solve():
    assert part1.solve() == 17435
