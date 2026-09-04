def part1(data: list[str]) -> int:
    rules, initial_state = parse_input(data)
    plants = get_initial_plants(initial_state)

    for _ in range(20):
        plants = next_generation(plants, rules)

    return sum(plants)


def part2(data: list[str]) -> int:
    TARGET_GENERATION = 50000000000

    rules, initial_state = parse_input(data)
    plants = get_initial_plants(initial_state)
    previous_sum = sum(plants)
    previous_diff = None
    stable_count = 0
    generation = 0

    while True:
        generation += 1
        plants = next_generation(plants, rules)
        current_sum = sum(plants)
        current_diff = current_sum - previous_sum

        if current_diff == previous_diff:
            stable_count += 1
        else:
            stable_count = 0
        if stable_count >= 5:
            break

        previous_sum = current_sum
        previous_diff = current_diff

    remaining_generations = TARGET_GENERATION - generation

    return current_sum + remaining_generations * current_diff


def next_generation(plants: set[int], rules: dict[str, str]) -> set[int]:
    new_plants = set()

    min_index = min(plants)
    max_index = max(plants)

    for i in range(min_index - 2, max_index + 3):
        pattern = ""

        for j in range(i - 2, i + 3):
            if j in plants:
                pattern += "#"
            else:
                pattern += "."

        if rules.get(pattern, ".") == "#":
            new_plants.add(i)

    return new_plants


def parse_input(data: list[str]) -> tuple[dict[str, str], str]:
    rules = {}
    initial_state = ""

    for line in data:
        if line.startswith("initial state:"):
            initial_state = line.split(": ")[1]
        elif " => " in line:
            pattern, result = line.split(" => ")
            rules[pattern] = result

    return rules, initial_state


def get_initial_plants(initial_state: str) -> set[int]:
    plants = set()

    for i, plant in enumerate(initial_state):
        if plant == "#":
            plants.add(i)

    return plants