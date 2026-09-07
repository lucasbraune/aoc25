import lib
import part1

EXAMPLE = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


def test_grand_total():
    actual = lib.grand_total(part1.parse_problems(EXAMPLE))
    assert actual == 4277556


def test_solve():
    assert part1.solve() == 5322004718681
