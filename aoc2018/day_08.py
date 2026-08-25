def part1(data: list[str]) -> int:
    numbers = list(map(int, data[0].split()))
    return parse_node(numbers)[0]


def part2(data: list[str]) -> int:
    numbers = list(map(int, data[0].split()))
    return parse_node(numbers)[1]


def parse_node(numbers: list[int]) -> tuple[int, int]:
    num_children = numbers.pop(0)
    num_metadata = numbers.pop(0)

    children = [parse_node(numbers) for _ in range(num_children)]
    metadata = [numbers.pop(0) for _ in range(num_metadata)]

    metadata_sum = sum(metadata)

    if not children:
        value = metadata_sum
    else:
        value = sum(
            children[index - 1][1]
            for index in metadata
            if 1 <= index <= len(children)
        )

    return (metadata_sum + sum(child[0] for child in children), value)
