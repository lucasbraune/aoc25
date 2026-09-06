# Advent of Code 2025, Day 2

## Notes

The sum of the lengths of the ranges in the input is about 10^6.

```python
def print_stats(ranges: list[Range]):
    min_log = 0.0
    max_log = 0.0
    for r in ranges:
        log = math.log10(r.end - r.start)
        if log < min_log:
            min_log = log
        if log > max_log:
            max_log = log
    print(f"min_log: {min_log}\nmax_log: {max_log}")
```
