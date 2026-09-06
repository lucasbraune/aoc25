import part2
from lib import Range

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


def test_union_step():
    ranges = [Range(3, 5), Range(10, 14), Range(16, 20)]
    r = Range(12, 18)

    actual = part2.union_step(ranges, r)

    assert actual == [Range(3, 5), Range(10, 20)]


def test_union():
    ranges = [Range(3, 5), Range(10, 14), Range(16, 20), Range(12, 18)]

    actual = part2.union(ranges)

    assert actual == [Range(3, 5), Range(10, 20)]


def test_cardinality():
    ranges = [Range(3, 5), Range(10, 14), Range(16, 20), Range(12, 18)]

    actual = part2.cardinality(ranges)

    assert actual == 14


def test_solve():
    assert part2.solve() == 338258295736104
