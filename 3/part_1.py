import re

from parse_input import parse_input

def extract_muls(str):
    return re.findall(r'mul\((\d+),(\d+)\)', str)

if __name__ == "__main__":
    sum = 0
    for a, b in extract_muls(parse_input()):
        print(a, b)
        sum+=(int(a)*int(b))

    print(sum)