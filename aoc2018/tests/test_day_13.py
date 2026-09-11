from aoc2018.day_13 import part1, part2


PART1_EXAMPLE = r"""/->-\
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   """.splitlines()


PART2_EXAMPLE = r"""/>-<\
|   |
| /<-+--\
| | | v
\>+</ |
  |   ^
  \<->/""".splitlines()


def test_part1():
    assert part1(PART1_EXAMPLE) == "7,3"


def test_part2():
    assert part2(PART2_EXAMPLE) == "6,4"