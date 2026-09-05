from pathlib import Path


def argmax(nums: list[int], *, start: int = 0, end: int | None = None) -> int:
    if not nums:
        raise ValueError("Argmax requires a non-empty array")
    if end == None:
        end = len(nums)
    argmax = start
    for k in range(start, end):
        if nums[k] > nums[argmax]:
            argmax = k
    return argmax


def joltage(bank: str) -> int:
    if len(bank) < 2:
        raise ValueError(f"Bad bank length: {len(bank)}")
    nums = [int(c) for c in bank]
    i = argmax(nums, end=len(nums) - 1)
    j = argmax(nums, start=i + 1)
    return nums[i] * 10 + nums[j]


def total_output(banks: str) -> int:
    return sum(joltage(bank) for bank in banks.split())


def solve() -> int:
    path = Path(".").parent / "resources" / "input.txt"
    with open(path) as file:
        return total_output(file.read())


if __name__ == "__main__":
    print(solve)
