from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, assert_never

INPUT = Path(__file__).resolve().parent.parent / "resources" / "input.txt"


def read_input() -> str:
    return INPUT.read_text()


def product(values: Iterable[int]) -> int:
    product = 1
    for x in values:
        product *= x
    return product


Operator = Literal["+", "*"]


def evaluate(operator: Operator, operands: Iterable[int]):
    if operator == "+":
        return sum(operands)
    elif operator == "*":
        return product(operands)
    else:
        assert_never(operator)


def ensure_operator(raw: str) -> Operator:
    if raw != "*" and raw != "+":
        raise ValueError(f"Bad operator: {raw}")
    return raw


@dataclass
class Problem:
    operands: list[int]
    operator: Operator


def grand_total(problems: Iterable[Problem]):
    return sum(evaluate(p.operator, p.operands) for p in problems)
