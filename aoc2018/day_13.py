def part1(input_data: list[str]) -> str:
    grid, carts = parse_input(input_data)

    while True:
        carts.sort(key=lambda cart: (cart.y, cart.x))
        for cart in carts:
            cart.move(grid)
            if has_collision(cart, carts):
                return f"{cart.x},{cart.y}"


def part2(input_data: list[str]) -> str:
    grid, carts = parse_input(input_data)

    while len(carts) > 1:
        carts.sort(key=lambda cart: (cart.y, cart.x))

        removed = set()

        for cart in carts:
            if cart in removed:
                continue

            cart.move(grid)

            for other in carts:
                if other == cart:
                    continue

                if other in removed:
                    continue

                same_position = cart.x == other.x and cart.y == other.y

                if same_position:
                    removed.add(cart)
                    removed.add(other)
                    break

        remaining_carts = []

        for cart in carts:
            if cart not in removed:
                remaining_carts.append(cart)

        carts = remaining_carts

    return f"{carts[0].x},{carts[0].y}"


def has_collision(cart, carts):
    for other in carts:
        if other != cart and cart.x == other.x and cart.y == other.y:
            return True
    return False


class Cart:
    def __init__(self, x: int, y: int, direction: str):
        self.x = x
        self.y = y
        self.direction = direction
        self.turns = 0

    def move(self, grid: list[list[str]]) -> None:
        self.move_forward()
        track = grid[self.y][self.x]
        if track == "/":
            self.handle_slash()
        elif track == "\\":
            self.handle_backslash()
        elif track == "+":
            self.handle_intersection()

    def move_forward(self) -> None:
        if self.direction == "^":
            self.y -= 1
        elif self.direction == "v":
            self.y += 1
        elif self.direction == "<":
            self.x -= 1
        elif self.direction == ">":
            self.x += 1

    def handle_slash(self) -> None:
        if self.direction == "^":
            self.direction = ">"
        elif self.direction == ">":
            self.direction = "^"
        elif self.direction == "v":
            self.direction = "<"
        elif self.direction == "<":
            self.direction = "v"

    def handle_backslash(self) -> None:
        if self.direction == "^":
            self.direction = "<"
        elif self.direction == "<":
            self.direction = "^"
        elif self.direction == "v":
            self.direction = ">"
        elif self.direction == ">":
            self.direction = "v"

    def handle_intersection(self) -> None:
        if self.turns == 0:
            self.turn_left()
        elif self.turns == 2:
            self.turn_right()
        self.turns += 1
        if self.turns == 3:
            self.turns = 0

    def turn_left(self) -> None:
        if self.direction == "^":
            self.direction = "<"
        elif self.direction == "<":
            self.direction = "v"
        elif self.direction == "v":
            self.direction = ">"
        elif self.direction == ">":
            self.direction = "^"

    def turn_right(self) -> None:
        if self.direction == "^":
            self.direction = ">"
        elif self.direction == ">":
            self.direction = "v"
        elif self.direction == "v":
            self.direction = "<"
        elif self.direction == "<":
            self.direction = "^"


def parse_input(input_data: list[str]) -> tuple[list[list[str]], list[Cart]]:
    width = max(len(line) for line in input_data)
    grid = []
    carts = []
    for y, line in enumerate(input_data):
        row = []
        line = line.ljust(width)
        for x, char in enumerate(line):
            if char in "^v<>":
                carts.append(Cart(x, y, char))
                if char in "^v":
                    row.append("|")
                else:
                    row.append("-")
            else:
                row.append(char)
        grid.append(row)
    return grid, carts