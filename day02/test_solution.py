from day02.solution import solve, Range, get_total_invalid_sum


def test_solve():
    ranges = [
        Range(start=11, end=22),
        Range(start=95, end=115),
        Range(start=998, end=1012),
        Range(start=1188511880, end=1188511890),
        Range(start=222220, end=222224),
        Range(start=1698522, end=1698528),
        Range(start=446443, end=446449),
        Range(start=38593856, end=38593862),
    ]
    assert get_total_invalid_sum(ranges) == 1227775554
