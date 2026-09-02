def part1(data: list[str]) -> str:
    points = parse_input(data)

    time = part2(data)

    xs = [x + vx * time for x, _, vx, _ in points]
    ys = [y + vy * time for _, y, _, vy in points]

    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = [[" " for _ in range(width)] for _ in range(height)]


    for x, y in zip(xs, ys):
        grid[y - min_y][x - min_x] = "#"

    message = "\n".join("".join(row) for row in grid)
    return f"\n{message}"


def part2(data: list[str]) -> int:
    points = parse_input(data)

    min_time = 0
    min_area = float("inf")
    current_time = 0

    while True:
        xs = [x + vx * current_time for x, _, vx, _ in points]
        ys = [y + vy * current_time for _, y, _, vy in points]

        width = max(xs) - min(xs)
        height = max(ys) - min(ys)
        area = width * height

        if area < min_area:
            min_area = area
            min_time = current_time
        else:
            break

        current_time += 1

    return min_time


def parse_input(data: list[str]) -> list[tuple[int, int, int, int]]:
    points = []

    for line in data:
        line = (
            line.replace("position=<", "")
            .replace("> velocity=<", ",")
            .replace(">", "")
        )

        x, y, vx, vy = map(int, line.split(","))
        points.append((x, y, vx, vy))

    return points