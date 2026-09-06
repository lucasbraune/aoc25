import lib
import part1


def from_matrix(diagram: list[list[str]]) -> str:
    return "\n".join(["".join(row) for row in diagram])


def test_remove():
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
    removed = lib.remove(diagram)
    assert removed == 13

    expected = """\
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x."""
    assert from_matrix(diagram) == expected


def test_solve():
    assert part1.solve() == 1433
