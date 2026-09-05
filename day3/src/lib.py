def argmax(nums: list[int], *, start: int = 0, end: int | None = None) -> int:
    if not nums:
        raise ValueError("Argmax requires a non-empty array")
    if end == None:
        end = len(nums)
    argmax = start
    for k in range(start + 1, end):
        if nums[k] > nums[argmax]:
            argmax = k
    return argmax


def make_decimal(nums: list[int]) -> int:
    res = 0
    for i in range(len(nums)):
        res += nums[i] * 10 ** (len(nums) - i - 1)
    return res


def joltage(bank: str, *, batteries: int) -> int:
    if batteries < 0:
        raise ValueError(f"Bad battery count: {batteries}")
    if len(bank) < batteries:
        raise ValueError(
            f"Bank is too small: bank_size={len(bank)} batteries={batteries}"
        )
    nums = [int(c) for c in bank]
    if batteries == 0:
        return 0
    start = 0
    positions = []
    for remaining in range(batteries, 0, -1):
        i = argmax(nums, start=start, end=len(nums) - remaining + 1)
        positions.append(i)
        start = i + 1
    return make_decimal([nums[i] for i in positions])


def total_output(banks: str, *, batteries: int) -> int:
    return sum(joltage(bank, batteries=batteries) for bank in banks.split())
