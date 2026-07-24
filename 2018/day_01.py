# Read input
changes = [int(line.strip()) for line in open('inputs/input_day_01.txt')]


# Part 1
print(sum(changes))


# Part 2
seen = {0}
frequency = 0
i = 0

while True:
    frequency += changes[i]
    if frequency in seen:
        print(frequency)
        break
    seen.add(frequency)
    i = (i + 1) % len(changes)