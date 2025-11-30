from .solution import distance_between_lists


list_1 = [1, 2, 3, 4, 5]
list_2 = [0, 0, 3, -1, 1]
diff = 12

print(zip(list_1, list_2))


def test_solution():
    assert distance_between_lists(list_1, list_2) == diff
