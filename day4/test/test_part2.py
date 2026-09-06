import lib
import part2


def test_iteratively_remove():
    input = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
    diagram = lib.to_matrix(input)

    removed: list[int] = part2.iteratively_remove(diagram)

    assert removed == [13, 12, 7, 5, 2, 1, 1, 1, 1]


def test_solve():
    assert part2.solve() == 8616
