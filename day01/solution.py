from pathlib import Path


input_data_path = Path(__file__).parent.resolve() / "input.txt"


def parse_lists(file_path: str) -> tuple[list[int], list[int]]:
    list_1, list_2 = [], []
    with open(file_path, "r") as f:
        for line in f:
            first, second = map(int, line.split())
            list_1.append(first)
            list_2.append(second)

    return list_1, list_2


def distance_between_lists(list_1: list[int], list_2: list[int]) -> int:
    sorted_1 = sorted(list_1)
    sorted_2 = sorted(list_2)

    return sum(abs(a - b) for a, b in zip(sorted_1, sorted_2))


def solve():
    list_1, list_2 = parse_lists(input_data_path)
    return distance_between_lists(list_1, list_2)
