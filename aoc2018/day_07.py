from collections import defaultdict


def parse_dependency(line: str) -> tuple[str, str]:
    return line[5], line[36]


def add_dependency(
    graph: dict[str, set[str]],
    in_degree: dict[str, int],
    prerequisite: str,
    dependent: str,
) -> None:
    graph[prerequisite].add(dependent)
    in_degree[dependent] += 1
    in_degree.setdefault(prerequisite, 0)


def get_available_steps(in_degree: dict[str, int]) -> set[str]:
    return {
        step
        for step, degree in in_degree.items()
        if degree == 0
    }
 

def decrease_degree(
    step: str,
    graph: dict[str, set[str]],
    in_degree: dict[str, int],
) -> None:
    for dependent in graph[step]:
        in_degree[dependent] -= 1


def remove_step(
    step: str,
    graph: dict[str, set[str]],
    in_degree: dict[str, int],
    available: set[str],
) -> None:
    for dependent in graph[step]:
        if in_degree[dependent] == 0:
            available.add(dependent)


def part1(data: list[str]) -> str:
    graph = defaultdict(set)
    in_degree = defaultdict(int)

    for line in data:
        prerequisite, dependent = parse_dependency(line)
        add_dependency(graph, in_degree, prerequisite, dependent)

    available = get_available_steps(in_degree)
    result = []

    while available:
        step = min(available)
        available.remove(step)
        result.append(step)
        decrease_degree(step, graph, in_degree)
        remove_step(step, graph, in_degree, available)

    return "".join(result)


def part2(data: list[str], num_workers: int = 5, base_time: int = 60) -> int:
    graph = defaultdict(set)
    in_degree = defaultdict(int)

    for line in data:
        prerequisite, dependent = parse_dependency(line)
        add_dependency(graph, in_degree, prerequisite, dependent)

    available = get_available_steps(in_degree)
    workers = [None] * num_workers
    time_remaining = [0] * num_workers
    total_time = 0

    while available or any(workers):
        for i in range(num_workers):
            if workers[i] is None and available:
                step = min(available)
                available.remove(step)
                workers[i] = step
                time_remaining[i] = base_time + (ord(step) - ord("A") + 1)

        total_time += 1

        for i in range(num_workers):
            if workers[i]:
                time_remaining[i] -= 1
                if time_remaining[i] == 0:
                    decrease_degree(workers[i], graph, in_degree)
                    remove_step(workers[i], graph, in_degree, available)
                    workers[i] = None

    return total_time
