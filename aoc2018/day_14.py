def part1(input_data: int) -> str:
    recipes = [3, 7]
    elf1 = 0
    elf2 = 1

    while len(recipes) < input_data + 10:
        elf1, elf2 = make_next_recipes(recipes, elf1, elf2)

    result = recipes[input_data:input_data + 10]
    return "".join(str(recipe) for recipe in result)

# Q: after recipe number N is on the board, what are the next 10 scores?


# P1
"""
- Start: recipes = [3, 7], elves at 0, 1
- Need 10 scores after N --> stop at len(recipes) >= N + 10
- Each round:
    1. add elves' scores
    2. append digits of sum (10 → [1, 0])
    3. move each elf: pos = (pos + score + 1) % len(recipes)
- Take recipes[N:N+10]
- Join digits --> answer
"""


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
        # last index where we would start if it was the last thing on the board
        if recipes[start:] == input_data:
            return start
        # did the pattern just land exactly at the end of the board?

        if recipes[start - 1:start - 1 + len(input_data)] == input_data:
            return start - 1
        # case where this round appended two digits, 
        # and the match actually completed right after the first 
        # of the two new digits

# Q: what's the first position where a given digit-sequence appears on the board?


# P2
"""
- Same setup + recipe generation as P1
- Convert input to digit list (preserve leading 0s)
- Loop until sequence appears:
    1. make next recipe(s)
    2. check last N digits
    3. also check N digits ending one position earlier
- Why 2 checks? One round can add 2 digits, so match may end
  after either the 1st or 2nd new digit
- Return number of recipes before the match
"""