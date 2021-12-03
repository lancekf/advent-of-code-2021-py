import os

input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

def findBitSums(list):
    sums = []

    for i in range(len(list[0])):
        sums.append(0)

    for num in list:
        for i in range(len(num)):
            b = -1 if num[i] == '0' else 1
            sums[i] = sums[i] + b
    
    return sums

def findRating(list, common, index):
    sums = findBitSums(list)

    bit = None
    if common:
        bit = '1' if sums[index] >= 0 else '0'
    else:
        bit = '0' if sums[index] >= 0 else '1'

    found = []
    for num in list:
        if num[index] == bit:
            found.append(num)

    if len(found) > 1:
        found = findRating(found, common, index+1)
    
    return found

o2Rating = int(findRating(input, True, 0)[0], 2)
print(f"o2: {o2Rating}")
co2Rating = int(findRating(input, False, 0)[0], 2)
print(f"co2: {co2Rating}")

print(f"life support: {o2Rating * co2Rating}")