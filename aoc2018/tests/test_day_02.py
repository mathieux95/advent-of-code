from aoc2018.day_02 import part1, part2


def test_part1() -> None:
    inp = [
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab",
    ]

    assert part1(inp) == 12


def test_part2() -> None:
    inp = [
        "abcde",
        "fghij",
        "klmno",
        "pqrst",
        "fguij",
        "axcye",
        "wvxyz",
    ]

    assert part2(inp) == "fgij"