input = open("resources/day1-input.txt").read().split("\n")

def sum(list):
    total = 0
    for n in list:
        total += int(n)
    return total

count = 0
for i in range(len(input)):
    if i >= 3:
        previous = sum(input[i-3:i])
        current = sum(input[i-2:i+1])

        if (previous < current):
            count += 1

print(count)