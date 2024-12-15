import re

from parse_input import parse_input

enabled = True

def execute_mult(m):
    a, b = m[4: -1].split(",")
    return int(a) * int(b)

sum = 0
for i in re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", parse_input()):
    if i == "do()":
        enabled = True
    elif i == "don't()":
        enabled = False
    else:
        if enabled:
            sum+=execute_mult(i)
print(sum)