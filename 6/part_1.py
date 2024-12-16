from parse_input import parse_input


def turn_90(dx, dy):
    return dy, -dx

start, map = parse_input()

def within_bounds(x, y):
    return all((x >= 0, x < len(map), y >= 0, y < len(map[0])))

x, y = start
dx, dy = (-1, 0)

visited = [[0 for i in m] for m in map]
visited[x][y] = 1

while within_bounds(x, y):
    visited[x][y] = 1

    if within_bounds(x+dx, y+dy):
        if map[x+dx][y+dy] == '#':
            dx, dy = turn_90(dx, dy)
        else:
            x, y = x + dx, y + dy 
    else:
        break

print(sum(sum(i) for i in visited))

    