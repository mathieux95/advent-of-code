def part1(data: list[str]) -> int:
    polymer = data[0]
    stack = []

    for unit in polymer:
        if stack and unit.swapcase() == stack[-1]:
            stack.pop()
        else:
            stack.append(unit)

    return len(stack)


def part2(data: list[str]) -> int:
    polymer = data[0]
    best_length = len(polymer)

    for unit in set(polymer.lower()):
        new_polymer = "".join(c for c in polymer if c.lower() != unit)
        best_length = min(best_length, part1([new_polymer]))

    return best_length


def part2(data: list[str]) -> int:
    polymer = data[0]

    return min(
        part1(["".join(c for c in polymer if c.lower() != unit)])
        for unit in set(polymer.lower())
    )