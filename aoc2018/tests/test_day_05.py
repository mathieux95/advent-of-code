from aoc2018.day_05 import part1, part2


def test_part1() -> None:
    example = [
        "dabAcCaCBAcCcaDA",
    ]
    assert part1(example) == 10


def test_part2() -> None:
    example = [
        "dabAcCaCBAcCcaDA",
    ]
    assert part2(example) == 4