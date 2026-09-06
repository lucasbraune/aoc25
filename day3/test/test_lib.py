import pytest

import lib


def test_argmax():
    arr = [1, 3, 2]
    assert lib.argmax(arr) == 1


@pytest.mark.parametrize(
    "digits, expected",
    [
        ([1, 2, 3], 123),
        ([5, 4], 54),
        ([5], 5),
    ],
)
def test_make_decimal(digits: list[int], expected: int):
    assert lib.make_decimal(digits) == expected


@pytest.mark.parametrize(
    "start, end",
    [
        (2, 2),  # empty range
        (5, 1),  # inverted range
        (0, 9),  # end past the array
        (-1, 3),  # negative start
    ],
)
def test_argmax_rejects_bad_range(start: int, end: int):
    with pytest.raises(ValueError):
        lib.argmax([1, 2, 3], start=start, end=end)


def test_argmax_rejects_empty_array():
    with pytest.raises(ValueError):
        lib.argmax([])


def test_joltage_rejects_negative_battery_count():
    with pytest.raises(ValueError):
        lib.joltage("123", batteries=-1)


def test_joltage_rejects_bank_smaller_than_battery_count():
    with pytest.raises(ValueError):
        lib.joltage("123", batteries=4)
