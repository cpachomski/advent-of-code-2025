from day01.solution import Move, count_zeros

moves = [
    Move(direction="R", turns=6),
    Move(direction="L", turns=12),
    Move(direction="R", turns=3),
    Move(direction="L", turns=20),
    Move(direction="R", turns=21),
    Move(direction="L", turns=1),
]


def test_solution():
    assert count_zeros(moves, 3) == 2
