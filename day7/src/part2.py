from dataclasses import dataclass

import lib


# Represents a beam segment at a `.`
@dataclass(frozen=True)
class Node:
    i: int
    j: int


class Graph:
    _diagram: list[list[str]]

    def __init__(self, diagram_str: str):
        self._diagram = lib.parse_diagram(diagram_str)

    def root(self) -> Node:
        return Node(0, self._diagram[0].index("S"))

    def children(self, node: Node) -> list[Node]:
        diagram = self._diagram
        rows = len(diagram)
        cols = len(diagram[1])
        i = node.i
        j = node.j

        if i + 1 >= rows:
            return []

        if diagram[i + 1][j] == ".":
            return [Node(i + 1, j)]
        elif diagram[i + 1][j] == "^":
            return [
                Node(i + 1, j + delta)
                for delta in [-1, +1]
                if (j + delta in range(cols) and diagram[i + 1][j + delta] == ".")
            ]
        else:
            raise Exception(f"Unexpected value at {(i + 1, j)}: {diagram[i + 1][j]}")


def count_paths(graph: Graph, node: Node, cache: dict[Node, int]) -> int:
    if cached := cache.get(node):
        return cached

    children = graph.children(node)
    result = sum(count_paths(graph, c, cache) for c in children) if children else 1

    cache[node] = result
    return result


def count_timelines(diagram_str: str) -> int:
    graph = Graph(diagram_str)
    return count_paths(graph, node=graph.root(), cache={})


def solve() -> int:
    return count_timelines(lib.read_input())


if __name__ == "__main__":
    print(solve())
