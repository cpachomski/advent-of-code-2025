from pathlib import Path
from typing import List
from dataclasses import dataclass
from itertools import chain


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


def is_invalid_num(num: int) -> bool:
    str_num = str(num)

    # Invalid numbers must have an even length
    if len(str_num) % 2 != 0:
        return False

    # Number is invalid if first half === second half
    else:
        first_half = str_num[0 : len(str_num) // 2]
        second_half = str_num[len(str_num) // 2 :]
        return first_half == second_half


def get_total_invalid_sum(ranges: List[Range]) -> int:
    all_nums_in_ranges = chain.from_iterable(range(r.start, r.end + 1) for r in ranges)

    all_invalid_nums = [num for num in all_nums_in_ranges if is_invalid_num(num)]

    return sum(all_invalid_nums)


def solve() -> int:
    path = Path(__file__).parent / "input.txt"
    ranges = get_ranges(path)
    return get_total_invalid_sum(ranges)
