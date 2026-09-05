import pytest

import lib
import part1


@pytest.mark.parametrize(
    "bank, expected",
    [
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
    ],
)
def test_joltage_with_2_batteries(bank: str, expected: int):
    assert lib.joltage(bank, batteries=2) == expected


def test_total_output_with_2_batteries():
    banks = """
    987654321111111
    811111111111119
    234234234234278
    818181911112111
    """
    print(banks)
    assert lib.total_output(banks, batteries=2) == 357


def test_solve():
    assert part1.solve() == 17435
