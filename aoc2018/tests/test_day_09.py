from aoc2018.day_09 import part1, part2

def test_part1() -> None:
    assert part1(["9 players; last marble is worth 25 points"]) == 32
    assert part1(["10 players; last marble is worth 1618 points"]) == 8317
    assert part1(["13 players; last marble is worth 7999 points"]) == 146373
    assert part1(["17 players; last marble is worth 1104 points"]) == 2764
    assert part1(["21 players; last marble is worth 6111 points"]) == 54718
    assert part1(["30 players; last marble is worth 5807 points"]) == 37305


def test_part2() -> None:
    assert part2(["9 players; last marble is worth 25 points"]) == 22563