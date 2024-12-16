from parse_input import parse_input

def turn_90(dx, dy):
    return dy, -dx

start, map = parse_input()

def within_bounds(x, y):
    return all((x >= 0, x < len(map), y >= 0, y < len(map[0])))

def has_loop(map, x, y, dx, dy):
    visited = set()

    while within_bounds(x, y):
        if (x, y, dx, dy) in visited:
            return True

        visited.add((x, y, dx, dy))

        if within_bounds(x+dx, y+dy):
            if map[x+dx][y+dy] == '#':
                dx, dy = turn_90(dx, dy)
            else:
                x, y = x + dx, y + dy 
        else:
            return False
    return False

def guard_paths(map, x, y, dx, dy):
    visited = [[0 for i in m] for m in map]

    while within_bounds(x, y):
        visited[x][y] = 1

        if within_bounds(x+dx, y+dy):
            if map[x+dx][y+dy] == '#':
                dx, dy = turn_90(dx, dy)
            else:
                x, y = x + dx, y + dy 
        else:
            break
    return [
        (i, j)
        for i, x in enumerate(visited)
        for j, y in enumerate(x)
        if y == 1
    ]

        


x, y = start
loop_count = 0

for i, j in guard_paths(map, x, y, -1, 0):
        original_value = map[i][j]
        if (i, j) == start or map[i][j] == "#":
            continue

        map[i][j] = '#'

        if has_loop(map, x, y, -1, 0):
            loop_count+=1

        map[i][j] = "."

print(loop_count)
        