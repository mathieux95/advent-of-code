def read_input(filename: str) -> list[str]:
    with open(filename) as file:
        return [line.strip() for line in file]


def parse_log(log: str) -> tuple[int, int, int, int, int, str]:
    timestamp, message = log.split("] ")
    date, time = timestamp[1:].split(" ")
    year, month, day = map(int, date.split("-"))
    hour, minute = map(int, time.split(":"))
    return year, month, day, hour, minute, message


def part1(logs: list[str]) -> int:
    guard_sleep = parse_guard_sleep(logs)

    total_sleep = {
        guard: sum(minutes)
        for guard, minutes in guard_sleep.items()
    }

    sleepiest_guard = max(total_sleep, key=total_sleep.get)
    sleepiest_minute = guard_sleep[sleepiest_guard].index(
        max(guard_sleep[sleepiest_guard])
    )

    return sleepiest_guard * sleepiest_minute


def part2(logs: list[str]) -> int:
    guard_sleep = parse_guard_sleep(logs)

    sleepiest_guard, sleepiest_minute = max(
        (
            (guard, minute)
            for guard, minutes in guard_sleep.items()
            for minute in range(60)
        ),
        key=lambda x: guard_sleep[x[0]][x[1]],
    )

    return sleepiest_guard * sleepiest_minute


def parse_guard_sleep(logs: list[str]) -> dict[int, list[int]]:
    guard_sleep = {}
    current_guard = None
    sleep_start = None

    for log in sorted(logs):
        *_, minute, message = parse_log(log)

        if "Guard" in message:
            current_guard = int(message.split()[1][1:])
            guard_sleep.setdefault(current_guard, [0] * 60)

        elif message == "falls asleep":
            sleep_start = minute

        else:
            for m in range(sleep_start, minute):
                guard_sleep[current_guard][m] += 1

    return guard_sleep