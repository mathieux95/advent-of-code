def part1(lines: list[str]) -> int:
    coordinates = split_lines(lines)
    min_x, max_x, min_y, max_y = bounds(coordinates)

    area_counts = {coord: 0 for coord in coordinates}
    infinite_coords = set()

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            distances = [(manhattan_distance((x, y), coord), coord) for coord in coordinates]
            distances.sort()

            if len(distances) > 1 and distances[0][0] == distances[1][0]:
                continue

            closest_coord = distances[0][1]
            area_counts[closest_coord] += 1

            if x in (min_x, max_x) or y in (min_y, max_y):
                infinite_coords.add(closest_coord)

    return max(count for coord, count in area_counts.items() if coord not in infinite_coords)


def part2(lines: list[str], threshold: int = 10000) -> int:
    coordinates = split_lines(lines)
    min_x, max_x, min_y, max_y = bounds(coordinates)

    safe_region_size = 0

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            total_distance = sum(
                manhattan_distance((x, y), coord)
                for coord in coordinates
            )

            if total_distance < threshold:
                safe_region_size += 1

    return safe_region_size


def split_lines(lines: list[str]) -> list[tuple[int, int]]:
    coordinates = []
    for line in lines:
        x, y = line.split(", ")
        coordinates.append((int(x), int(y)))
    return coordinates


def bounds(coordinates: list[tuple[int, int]]) -> tuple[int, int, int, int]:
    min_x = min(x for x, y in coordinates)
    max_x = max(x for x, y in coordinates)
    min_y = min(y for x, y in coordinates)
    max_y = max(y for x, y in coordinates)

    return min_x, max_x, min_y, max_y


def manhattan_distance(first: tuple[int, int], second: tuple[int, int]) -> int:
    x1, y1 = first
    x2, y2 = second
    return abs(x1 - x2) + abs(y1 - y2)