import pytest

import lib
import part2


@pytest.mark.parametrize(
    "range, expected",
    [
        ("11-22", [11, 22]),
        ("95-115", [99, 111]),
        ("998-1012", [999, 1010]),
        ("1188511880-1188511890", [1188511885]),
        ("222220-222224", [222222]),
        ("1698522-1698528", []),
        ("446443-446449", [446446]),
        ("38593856-38593862", [38593859]),
        ("565653-565659", [565656]),
        ("824824821-824824827", [824824824]),
        ("2121212118-2121212124", [2121212121]),
    ],
)
def test_invalid_ids(range, expected):
    parsed = lib.parse_range(range)
    assert part2.invalid_ids(parsed) == expected


@pytest.mark.parametrize(
    "s, seq_len, expected",
    [
        ("11", 1, True),
        ("111", 1, True),
        ("1010", 2, True),
        ("1010", 3, False),
        ("1188511885", 5, True),
        ("222222", 1, True),
        ("2121212121", 2, True),
    ],
)
def test_has_repeated_sequence(s: str, seq_len: int, expected: bool):
    assert part2.has_repeated_sequence(s, seq_len) == expected


# @pytest.mark.skip(reason="Correct, but slow")
def test_solve():
    assert part2.solve() == 70187097315
