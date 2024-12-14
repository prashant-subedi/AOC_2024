from parse_input import parse_input
a, b = parse_input()

diff = 0
for i, j in zip(sorted(a), sorted(b)):
    diff += abs(i - j)
print(diff)