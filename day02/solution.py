from pathlib import Path
from typing import List
from dataclasses import dataclass


@dataclass(frozen=True)
class Range:
    start: int
    end: int


def get_ranges(file_path: str) -> List[Range]:
    with open(file_path, "r") as f:
        return [
            Range(start=int(start), end=int(end))
            for r in f.read().split(",")
            for start, end in [r.split("-")]
        ]


def has_even_num_of_digits(num: int) -> bool:
    return len(str(num)) % 2 == 0


def is_invalid_num(num: int) -> bool:
    # Invalid numbers must have an even length
    if not has_even_num_of_digits(num):
        return False
    else:
        str_num = str(num)
        first_half = str_num[0 : len(str_num) // 2]
        second_half = str_num[len(str_num) // 2 :]
        return first_half == second_half


def get_invalid_range_sum(r: Range) -> int:
    invalid_sum = 0
    for num in range(r.start, r.end + 1):
        if is_invalid_num(num):
            invalid_sum += num

    return invalid_sum


def get_total_invalid_sum(ranges: List[Range]) -> int:
    invalid_sum = 0
    for r in ranges:
        invalid_sum += get_invalid_range_sum(r)
    return invalid_sum


def solve() -> int:
    path = Path(__file__).parent / "input.txt"
    ranges = get_ranges(path)
    return get_total_invalid_sum(ranges)
