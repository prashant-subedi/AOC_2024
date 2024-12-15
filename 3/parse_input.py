def parse_input():
    with open("input.txt", "r") as file:
        return file.read()
    
if __name__ == "__main__":
    a = parse_input()
    print(a)
