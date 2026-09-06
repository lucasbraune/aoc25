import lib


def solve() -> int:
    diagram = lib.to_matrix(lib.read_input())
    return lib.remove(diagram)


if __name__ == "__main__":
    print(solve())
