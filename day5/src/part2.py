from collections.abc import Callable, Iterable

import lib
from lib import Range


def have_overlap(left: Range, right: Range) -> bool:
    if left.start > right.start:
        left, right = right, left
    return left.end >= right.start


def partition[T](
    values: Iterable[T], predicate: Callable[[T], bool]
) -> tuple[list[T], list[T]]:
    """Splits values into those satisfying the predicate and those that don't."""
    yes: list[T] = []
    no: list[T] = []
    for value in values:
        if predicate(value):
            yes.append(value)
        else:
            no.append(value)
    return yes, no


# Returns the ranges in the union of `ranges` with `next`. The returned ranges are
# disjoint ranges if the ranges in `ranges` are disjoint
def union_step(ranges: Iterable[Range], next: Range) -> list[Range]:
    overlapping, non_overlapping = partition(ranges, lambda r: have_overlap(next, r))

    if overlapping:
        start = min(next.start, min(a.start for a in overlapping))
        end = max(next.end, max(a.end for a in overlapping))
        overlapping_union_next = Range(start, end)
    else:
        overlapping_union_next = next

    # overlapping_union is disjoint from non_overlapping
    return non_overlapping + [overlapping_union_next]


def union(ranges: Iterable[Range]) -> list[Range]:
    acc = []
    for r in ranges:
        acc = union_step(acc, r)
    return acc


def cardinality(ranges: Iterable[Range]) -> int:
    return sum(r.cardinality() for r in union(ranges))


def solve() -> int:
    ranges = lib.parse_input(lib.read_input()).ranges
    return cardinality(ranges)


if __name__ == "__main__":
    print(solve())
