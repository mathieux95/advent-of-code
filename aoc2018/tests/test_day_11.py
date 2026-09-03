from aoc2018.day_11 import part1, part2

def test_part1():
    assert part1(18) == (33, 45)
    assert part1(42) == (21, 61)

def test_part2():
    assert part2(18) == (90, 269, 16)
    assert part2(42) == (232, 251, 12)