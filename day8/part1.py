import os

input = open(f"{os.path.dirname(__file__)}/input.txt").read().split("\n")

def main():

    unique = {2:1, 4:4, 3:7, 7:8}

    count = 0
    for line in input:
        split = line.split(' | ')
        digits = split[1].split(' ')

        for digit in digits:
            if len(digit) in unique:
                count += 1
    
    print(count)

main()