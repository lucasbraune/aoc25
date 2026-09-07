import lib
import part2

EXAMPLE = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


def test_grand_total():
    actual = lib.grand_total(part2.parse_problems(EXAMPLE))
    assert actual == 3263827


def test_solve():
    assert part2.solve() == 9876636978528
