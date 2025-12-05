from pathlib import Path
from typing import List


def get_banks(file_path: Path) -> List[List[int]]:
    with open(file_path, "r") as f:
        return [list(map(int, line.strip())) for line in f.readlines()]


def total_joltages(banks: List[List[int]]) -> int:
    total = 0
    for bank in banks:
        first_largest = max(bank[: len(bank) - 1])
        find_second_start = bank.index(first_largest) + 1
        second_largest = max(bank[find_second_start:])
        total += int(str(first_largest) + str(second_largest))

    return total


def solve() -> int:
    file_path = Path(__file__).parent / "input.txt"
    banks = get_banks(file_path)
    return total_joltages(banks)
