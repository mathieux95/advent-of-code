def parse_log(log: str) -> tuple[str, int, int, int, int]:
    timestamp, message = log.split("] ")
    date, time = timestamp[1:].split(" ")
    year, month, day = map(int, date.split("-"))
    hour, minute = map(int, time.split(":"))
    return year, month, day, hour, minute, message


def part1(logs: list[str]) -> int:
    guard_sleep = {}
    total_sleep = {}
    current_guard = None
    sleep_start = None

    for log in sorted(logs):
        *_, minute, message = parse_log(log)

        if "Guard" in message:
            current_guard = int(message.split()[1][1:])
            guard_sleep.setdefault(current_guard, [0] * 60)
            total_sleep.setdefault(current_guard, 0)

        elif message == "falls asleep":
            sleep_start = minute

        else:
            total_sleep[current_guard] += minute - sleep_start
            for m in range(sleep_start, minute):
                guard_sleep[current_guard][m] += 1

    sleepiest_guard = max(total_sleep, key=total_sleep.get)
    minutes = guard_sleep[sleepiest_guard]
    sleepiest_minute = minutes.index(max(minutes))

    return sleepiest_guard * sleepiest_minute


def part2(logs: list[str]) -> int:
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

        else:  # wakes up
            for m in range(sleep_start, minute):
                guard_sleep[current_guard][m] += 1

    max_count = 0
    sleepiest_guard = None
    sleepiest_minute = None

    for guard, minutes in guard_sleep.items():
        for minute, count in enumerate(minutes):
            if count > max_count:
                max_count = count
                sleepiest_guard = guard
                sleepiest_minute = minute

    return sleepiest_guard * sleepiest_minute
