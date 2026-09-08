import lib
import part1


def test_evolve(initial_state: str, end_state: str):
    diagram = lib.parse_diagram(initial_state)

    part1.evolve(diagram)

    assert lib.render_diagram(diagram) == end_state


def test_count_splits(initial_state: str):
    assert part1.count_splits(initial_state) == 21


def test_solve():
    assert part1.solve() == 1681
