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
