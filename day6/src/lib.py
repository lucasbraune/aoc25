from collections.abc import Iterable
from dataclasses import dataclass
from math import prod
from pathlib import Path
from typing import Literal

INPUT = Path(__file__).resolve().parent.parent / "resources" / "input.txt"


def read_input() -> str:
    return INPUT.read_text()


Operator = Literal["+", "*"]


def evaluate(operator: Operator, operands: Iterable[int]) -> int:
    match operator:
        case "+":
            return sum(operands)
        case "*":
            return prod(operands)


def ensure_operator(raw: str) -> Operator:
    match raw:
        case "+" | "*":
            return raw
        case _:
            raise ValueError(f"Bad operator: {raw}")


@dataclass
class Problem:
    operands: list[int]
    operator: Operator


def grand_total(problems: Iterable[Problem]) -> int:
    return sum(evaluate(p.operator, p.operands) for p in problems)
