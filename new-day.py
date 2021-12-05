import sys
import os

day = int(sys.argv[1])

assert day > 0, f"Day must be greater than 0, was: {day}"

day = f"day{day}"

os.makedirs(day, exist_ok=True)

f = open(f"{day}/part1.py", "w")
f.write('''import os

input = open(f"{os.path.dirname(__file__)}/input-test.txt").read().split("\\n")

''')

open(f"{day}/part2.py", "w")
open(f"{day}/input.txt", "w")
open(f"{day}/input-test.txt", "w")