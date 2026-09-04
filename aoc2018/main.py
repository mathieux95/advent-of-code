import argparse
from pathlib import Path

from aoc2018 import day_01, day_02, day_03, day_04, day_05, day_06, day_07, day_08, day_09, day_10, day_11, day_12

DAYS = {
    1: day_01,
    2: day_02,
    3: day_03,
    4: day_04,
    5: day_05,
    6: day_06,
    7: day_07,
    8: day_08,
    9: day_09,
    10: day_10,
    11: day_11,
    12: day_12,

}

PACKAGE_DIR = Path(__file__).resolve().parent


def load_day_input(day: int) -> list[str] | int:
    path = PACKAGE_DIR / "inputs" / f"input_day_{day:02d}.txt"
    with path.open() as file:
        lines = [line.strip() for line in file if line.strip()]
    if len(lines) == 1:
        try:
            return int(lines[0])
        except ValueError:
            pass

    return lines


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

        module = DAYS[day]
        data = load_day_input(day)

        print(f"Day {day} - Part 1: {module.part1(data)}")
        print(f"Day {day} - Part 2: {module.part2(data)}")

if __name__ == "__main__":
    main()