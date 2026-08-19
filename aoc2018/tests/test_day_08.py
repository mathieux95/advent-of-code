from aoc2018.day_08 import part1, part2

def test_part1() -> None:
    assert part1(["2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"]) == 138

def test_part2() -> None:
    assert part2(["2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"]) == 66
