import lib
import part1
from lib import Input, Range

EXAMPLE = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


def test_parse_input():
    actual = lib.parse_input(EXAMPLE)

    expected = Input(
        ranges=[
            Range(3, 5),
            Range(10, 14),
            Range(16, 20),
            Range(12, 18),
        ],
        available=[1, 5, 8, 11, 17, 32],
    )
    assert actual == expected


def test_fresh_ingredients():
    actual = part1.fresh_ingredients(lib.parse_input(EXAMPLE))

    assert actual == [5, 11, 17]


def test_solve():
    assert part1.solve() == 617
