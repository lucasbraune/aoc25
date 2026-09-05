import pytest

import lib
import part2


@pytest.mark.parametrize(
    "bank, expected",
    [
        ("987654321111111", 987654321111),
        ("811111111111119", 811111111119),
        ("234234234234278", 434234234278),
        ("818181911112111", 888911112111),
    ],
)
def test_joltage_with_12_batteries(bank: str, expected: int):
    assert lib.joltage(bank, batteries=12) == expected


def test_total_output_with_12_batteries():
    banks = """
    987654321111111
    811111111111119
    234234234234278
    818181911112111
    """
    print(banks)
    assert lib.total_output(banks, batteries=12) == 3121910778619

def test_solve():
    assert part2.solve() == 172886048065379
