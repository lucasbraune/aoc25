from pathlib import Path

INPUT = Path(__file__).resolve().parent.parent / "resources" / "input.txt"


def read_input() -> str:
    return INPUT.read_text()


def argmax(nums: list[int], *, start: int = 0, end: int | None = None) -> int:
    if end is None:
        end = len(nums)
    if not 0 <= start < end <= len(nums):
        raise ValueError(
            f"Argmax requires a non-empty range within the array: "
            f"start={start} end={end} len={len(nums)}"
        )
    best = start
    for k in range(start + 1, end):
        if nums[k] > nums[best]:
            best = k
    return best


def make_decimal(digits: list[int]) -> int:
    res = 0
    for d in digits:
        res = res * 10 + d
    return res


def joltage(bank: str, *, batteries: int) -> int:
    if batteries < 0:
        raise ValueError(f"Bad battery count: {batteries}")
    if len(bank) < batteries:
        raise ValueError(
            f"Bank is too small: bank_size={len(bank)} batteries={batteries}"
        )
    if batteries == 0:
        return 0
    nums = [int(c) for c in bank]
    start = 0
    positions = []
    for remaining in range(batteries, 0, -1):
        i = argmax(nums, start=start, end=len(nums) - remaining + 1)
        positions.append(i)
        start = i + 1
    return make_decimal([nums[i] for i in positions])


def total_output(banks: str, *, batteries: int) -> int:
    return sum(joltage(bank, batteries=batteries) for bank in banks.split())
