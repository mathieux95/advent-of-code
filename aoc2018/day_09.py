def part1(data: list[str]) -> int:
    num_players, last_marble = parse_input(data)
    return play(num_players, last_marble)


def part2(data: list[str]) -> int:
    num_players, last_marble = parse_input(data)
    return play(num_players, last_marble * 100)


def parse_input(data: list[str]) -> tuple[int, int]:
    parts = data[0].split()
    num_players = int(parts[0])
    last_marble = int(parts[6])
    return num_players, last_marble


def play(num_players: int, last_marble: int) -> int:
    circle = [0]
    current = 0
    scores = [0] * num_players

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            current = (current - 7) % len(circle)
            scores[marble % num_players] += marble + circle.pop(current)
        else:
            current = (current + 2) % len(circle)
            circle.insert(current, marble)

    return max(scores)
