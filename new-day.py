import sys

day = int(sys.argv[1])

assert day > 0, f"Day must be greater than 0, was: {day}"

open(f"day{day}.py", "w")
open(f"resources/day{day}-input.py", "w")
open(f"resources/day{day}-input-test.py", "w")