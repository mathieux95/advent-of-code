from aoc2018.day_03 import part1, part2

def test_part1() -> None:
    example = [
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 5,5: 2x2",
    ]
    assert part1(example) == 4


def test_part2() -> None:
    example = [
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 5,5: 2x2",
    ]
    assert part2(example) == 3