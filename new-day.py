import sys

day = int(sys.argv[1])

assert day > 0, f"Day must be greater than 0, was: {day}"

f = open(f"day{day}.py", "w")
f.write(f'input = open("resources/day{day}-input-test.txt").read().split("\\n")\n\n')

open(f"resources/day{day}-input.py", "w")
open(f"resources/day{day}-input-test.py", "w")