def part1(changes: list[int]) -> int:
    return sum(changes)


def part2(changes: list[int]) -> int:
    seen = {0}
    frequency = 0
    i = 0

    while True:
        frequency += changes[i]
        if frequency in seen:
            return frequency
        seen.add(frequency)
        i = (i + 1) % len(changes)
