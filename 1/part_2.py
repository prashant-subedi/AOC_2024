from collections import Counter
from parse_input import parse_input

a, b = parse_input()

b_count = Counter(b)

similarity_score = 0
for i in a:
    similarity_score += i * b_count[i]

print(similarity_score)