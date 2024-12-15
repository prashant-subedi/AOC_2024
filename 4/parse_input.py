def parse_input():
    with open("input.txt") as f:
        return [i.strip() for i in f]
            
if __name__ == "__main__":
    print(parse_input())