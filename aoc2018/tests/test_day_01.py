from aoc2018.day_01 import part1, part2

def test_part1() -> None:
    assert part1([1, 2, 3]) == 6
    assert part1([1, 9, -2]) == 8
    assert part1([9, 7, -3]) == 13


def test_part2() -> None:
    assert part2([1, -1]) == 0
    assert part2([3, 3, 4, -2, -4]) == 10
    assert part2([-6, 3, 8, 5, -6]) == 5
    assert part2([7, 7, -2, -7, -4]) == 14