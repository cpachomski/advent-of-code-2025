from pathlib import Path
from typing import Literal
from dataclasses import dataclass


@dataclass(frozen=True)
class Move:
    direction: Literal["L", "R"]
    turns: int


input_data_path = Path(__file__).parent.resolve() / "input.txt"


def get_moves(file_path: str) -> list[Move]:
    moves = []
    with open(file_path, "r") as f:
        for line in f:
            chars = list(line)
            direction = chars[0]
            turns = int("".join(chars[1:]))
            moves.append(Move(direction=direction, turns=turns))

    return moves


def turn(current, move) -> int:
    if move.direction == "R":
        return (current + move.turns - 100) % 100
    elif move.direction == "L":
        return (current - move.turns - 100) % 100


def count_zeros(moves: list[Move], start: int) -> int:
    current = start
    zeros = 0
    for move in moves:
        current = turn(current, move)
        if current == 0:
            zeros += 1

    return zeros


def solve():
    start = 50
    moves = get_moves(input_data_path)
    return count_zeros(moves, start)
