from collections import defaultdict

def parse_input():
    with open("input.txt") as f:
        a = []
        position = None
        for i, line in enumerate(f):
            b = []
            for j, c in enumerate(line.strip()):
                if c == "^":
                    b.append(".")
                    position = i, j
                else:
                    b.append(c)
            a.append(b)
        return position, a
                
                    

if __name__ == "__main__":
    print(parse_input())