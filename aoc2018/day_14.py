def part1(input_data: int) -> str:
    recipes = [3, 7]
    elf1 = 0
    elf2 = 1

    while len(recipes) < input_data + 10:
        elf1, elf2 = make_next_recipes(recipes, elf1, elf2)

    result = recipes[input_data:input_data + 10]
    return "".join(str(recipe) for recipe in result)

# Q: after recipe number N is on the board, what are the next 10 scores?

def make_next_recipes(recipes, elf1, elf2):
    total = recipes[elf1] + recipes[elf2]

    if total >= 10:
        recipes.append(1)

    recipes.append(total % 10)

    elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
    elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)

    return elf1, elf2


def part2(input_data: str) -> int:
    recipes = [3, 7]
    elf1 = 0
    elf2 = 1

    input_data = list(map(int, str(input_data)))

    while True:
        elf1, elf2 = make_next_recipes(recipes, elf1, elf2)

        start = len(recipes) - len(input_data)
        if recipes[start:] == input_data:
            return start

        if recipes[start - 1:start - 1 + len(input_data)] == input_data:
            return start - 1
            
# Q: what's the first position where a given digit-sequence appears on the board?
