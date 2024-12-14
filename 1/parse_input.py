def parse_input():
    a, b = [], []
    with open("input.txt", "r") as file:
        for i in file:
            a.append(int(i.split()[0]))
            b.append(int(i.split()[1]))
    return a, b

if __name__ == "__main__":
    a, b = parse_input()
    print(a, b)