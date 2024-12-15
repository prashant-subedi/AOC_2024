def parse_input():
    with open("input.txt", "r") as file:
        a = []
        for line in file:
            a.append([int(line.strip()) for line in line.split(" ")])
        return a

if __name__ == "__main__":
    a = parse_input()
    print(a)
