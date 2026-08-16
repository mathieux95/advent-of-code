import argparse

from aoc2018 import day_01, day_02, day_03


DAYS = {
    1: day_01,
    2: day_02,
    3: day_03,
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "days",
        type=int,
        nargs="+",
        help="Advent of Code days to run"
    )

    args = parser.parse_args()

    for day in args.days:
        if day not in DAYS:
            raise ValueError(f"Day {day} is not implemented yet.")

        day_module = DAYS[day]

        input_file = f"inputs/input_day_{day:02d}.txt"

        data = day_module.read_input(input_file)

        print(f"Day {day} - Part 1: {day_module.part1(data)}")
        print(f"Day {day} - Part 2: {day_module.part2(data)}")


if __name__ == "__main__":
    main()