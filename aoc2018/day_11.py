def part1(grid_serial_number: int) -> tuple[int, int]:
    max_power = float('-inf')
    max_coord = (0, 0)

    for x in range(1, 299):
        for y in range(1, 299):
            total_power = sum(
                calculate_power_level(x + dx, y + dy, grid_serial_number)
                for dx in range(3)
                for dy in range(3)
            )
            if total_power > max_power:
                max_power = total_power
                max_coord = (x, y)

    return max_coord


def part2(grid_serial_number: int) -> tuple[int, int, int]:
    max_power = float('-inf')
    max_coord_size = (0, 0, 0)

    for size in range(1, 301):
        for x in range(1, 302 - size):
            for y in range(1, 302 - size):
                total_power = sum(
                    calculate_power_level(x + dx, y + dy, grid_serial_number)
                    for dx in range(size)
                    for dy in range(size)
                )
                if total_power > max_power:
                    max_power = total_power
                    max_coord_size = (x, y, size)

    return max_coord_size


def calculate_power_level(x: int, y: int, grid_serial_number: int) -> int:
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_serial_number
    power_level *= rack_id

    return (power_level // 100) % 10 - 5

def parse_input(data: list[str]) -> int:
    return int(data[0])