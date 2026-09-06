import pytest

import lib
import part1


@pytest.mark.parametrize(
    "range, expected",
    [
        ("11-22", [11, 22]),
        ("95-115", [99]),
        ("998-1012", [1010]),
        ("1188511880-1188511890", [1188511885]),
        ("222220-222224", [222222]),
        ("1698522-1698528", []),
        ("446443-446449", [446446]),
        ("38593856-38593862", [38593859]),
        ("565653-565659", []),
        ("824824821-824824827", []),
        ("2121212118-2121212124", []),
    ],
)
def test_invalid_ids(range, expected):
    parsed = lib.parse_range(range)
    assert part1.invalid_ids(parsed) == expected


# @pytest.mark.skip(reason="Correct, but slow")
def test_solve():
    assert part1.solve() == 54234399924
