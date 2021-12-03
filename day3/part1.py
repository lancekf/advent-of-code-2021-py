import os

input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

sums = []

for i in range(len(input[0])):
    sums.append(0)

for num in input:
    for i in range(len(num)):
        b = -1 if num[i] == '0' else 1
        sums[i] = sums[i] + b

gammaBits = []
epsilonBits = []

for i in range(len(sums)):
    power = 1 if sums[i] > 0 else 0

    # Append as strings to later join
    gammaBits.append(f'{1 ^ power}')
    epsilonBits.append(f'{0 ^ power}')

gamma = int(''.join(gammaBits), 2)
epsilon = int(''.join(epsilonBits), 2)

print(f"Gamma: {gamma}")
print(f"Epsilon: {epsilon}")
print(f"Power Consumption: {gamma * epsilon}")