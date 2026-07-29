# Part 1
num_twos = 0
num_threes = 0

with open("inputs/input_day_02.txt") as x:
    for line in x:
        counts = {}
        for char in line.strip():
            counts[char] = counts.get(char, 0) + 1

        if 2 in counts.values():
            num_twos += 1
        if 3 in counts.values():
            num_threes += 1

print(num_twos * num_threes)


# Part 2 
with open("inputs/input_day_02.txt") as x:
    lines = [line.strip() for line in x]
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            diff = 0
            common = []
            for a, b in zip(lines[i], lines[j]):
                if a != b:
                    diff += 1
                else:
                    common.append(a)
            if diff == 1:
                print("".join(common))
                break
            