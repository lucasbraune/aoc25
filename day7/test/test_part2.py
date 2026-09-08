import part2


def test_count_timelines(initial_state: str):
    actual = part2.count_timelines(initial_state)
    assert actual == 40


def test_solve():
    assert part2.solve() == 422102272495018
