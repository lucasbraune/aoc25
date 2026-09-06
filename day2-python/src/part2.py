from lib import Range, parse_input, read_input


def has_repeated_sequence(s: str, seq_len: int) -> bool:
    if seq_len < 1 or seq_len > len(s):
        raise ValueError(f"Bad seq_len: {seq_len}")
    if len(s) % seq_len != 0:
        return False
    seq_count = len(s) // seq_len

    return all(
        all(s[i] == s[j * seq_len + i] for j in range(1, seq_count))
        for i in range(0, seq_len)
    )


def is_invalid(x: int) -> bool:
    s = str(x)
    return any(
        has_repeated_sequence(s, seq_len) for seq_len in range(1, len(s) // 2 + 1)
    )


def invalid_ids(r: Range) -> list[int]:
    return [x for x in range(r.start, r.end + 1) if is_invalid(x)]


def solve() -> int:
    ranges = parse_input(read_input())
    return sum(sum(invalid_ids(r)) for r in ranges)


if __name__ == "__main__":
    print(solve())
