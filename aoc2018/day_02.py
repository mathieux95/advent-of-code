def read_input(filename: str) -> list[str]:
    with open(filename) as file:
        return [line.strip() for line in file]


def part1(box_ids: list[str]) -> int:
    num_twos = 0
    num_threes = 0

    for box_id in box_ids:
        counts = {}

        for char in box_id:
            counts[char] = counts.get(char, 0) + 1

        if 2 in counts.values():
            num_twos += 1

        if 3 in counts.values():
            num_threes += 1

    return num_twos * num_threes


def part2(box_ids: list[str]) -> str:
    for i, box_id in enumerate(box_ids):
        for other_id in box_ids[i + 1:]:
            diff = 0
            common = []

            for a, b in zip(box_id, other_id):
                if a != b:
                    diff += 1
                else:
                    common.append(a)

            if diff == 1:
                return "".join(common)

    return ""