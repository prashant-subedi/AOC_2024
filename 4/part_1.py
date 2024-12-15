from parse_input import parse_input

PATTERN = "XMAS"
DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, 1),
    (1, -1),
    (-1, -1)
]

def find_xmas_pattern(data, match_position, direction, match_length):
    if match_length == len(PATTERN):
        return True
    if match_position[0] < 0 or match_position[0] >= len(data):
        return False
    if match_position[1] < 0 or match_position[1] >= len(data[0]):
        return False
    if data[match_position[0]][match_position[1]] != PATTERN[match_length]:
        return False
    return find_xmas_pattern(
            data, 
            (match_position[0] + direction[0], match_position[1] + direction[1]),
            direction,
            match_length+1
    )


count = 0
data = parse_input()

for i, line in enumerate(data):
    for j, char in enumerate(line):
        for direction in DIRECTIONS:
            if find_xmas_pattern(data, (i, j), direction, 0):
                count+=1


print(count)
        