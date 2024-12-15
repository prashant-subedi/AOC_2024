from parse_input import parse_input

count = 0
data = parse_input()

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if data[i][j] == 'A':
            if any((i==0, j==0, i == len(data) -1, j == len(data[0]) - 1)):
                continue
            if (
                {data[i-1][j-1], data[i+1][j+1]} == {'M', 'S'}
                and {data[i-1][j+1], data[i+1][j-1]} == {'M', 'S'}
            ):
                count+=1

print(count)
        