import lib


def iteratively_remove(diagram: list[list[str]]) -> list[int]:
    result = []
    while removed := lib.remove(diagram):
        result.append(removed)
    return result


def solve() -> int:
    diagram = lib.to_matrix(lib.read_input())
    removed: list[int] = iteratively_remove(diagram)
    return sum(r for r in removed)


if __name__ == "__main__":
    print(solve())
