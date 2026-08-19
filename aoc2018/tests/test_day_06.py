from aoc2018.day_06 import part1, part2

def test_part1() -> None:
    example = [
        "1, 1",
        "1, 6",
        "8, 3",
        "3, 4",
        "5, 5",
        "8, 9",
    ]
    assert part1(example) == 17


def test_part2() -> None:
    example = [
        "1, 1",
        "1, 6",
        "8, 3",
        "3, 4",
        "5, 5",
        "8, 9",
    ]
    assert part2(example) == 16
