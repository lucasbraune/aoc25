from lib import read_input, total_output


def solve() -> int:
    return total_output(read_input(), batteries=2)


if __name__ == "__main__":
    print(solve())
