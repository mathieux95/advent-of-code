def read_input(filename: str) -> list[str]:
    with open(filename) as file:
        return [line.strip() for line in file]


def parse_claim(claim: str) -> tuple[int, int, int, int, int]:
    claim_id, _, position, size = claim.split()
    left, top = map(int, position[:-1].split(","))
    width, height = map(int, size.split("x"))
    return int(claim_id[1:]), left, top, width, height


def part1(claims: list[str]) -> int:
    fabric = {}

    for claim in claims:
        _, left, top, width, height = parse_claim(claim)

        for x in range(left, left + width):
            for y in range(top, top + height):
                fabric[(x, y)] = fabric.get((x, y), 0) + 1

    return sum(1 for count in fabric.values() if count > 1)


def part2(claims: list[str]) -> int:
    fabric = {}
    claim_ids = set()

    for claim in claims:
        claim_id, left, top, width, height = parse_claim(claim)
        claim_ids.add(claim_id)

        for x in range(left, left + width):
            for y in range(top, top + height):
                if (x, y) in fabric:
                    fabric[(x, y)].append(claim_id)
                else:
                    fabric[(x, y)] = [claim_id]

    for claim_list in fabric.values():
        if len(claim_list) > 1:
            for claim_id in claim_list:
                claim_ids.discard(claim_id)

    return claim_ids.pop() if claim_ids else -1
