from lib import Range, parse_input, read_input


def is_invalid(x: int) -> bool:
    s = str(x)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return all(s[i] == s[mid + i] for i in range(0, mid))


def invalid_ids(r: Range) -> list[int]:
    return [x for x in range(r.start, r.end + 1) if is_invalid(x)]


def solve() -> int:
    ranges = parse_input(read_input())
    return sum(sum(invalid_ids(r)) for r in ranges)


if __name__ == "__main__":
    print(solve())
