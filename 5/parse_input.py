from collections import defaultdict

def parse_input():
    with open("input.txt") as f:
        raw_rules, raw_updates =  f.read().split("\n\n")
        expanded_rules = list(
            [int(j) for j in (i.split('|'))]
            for i in raw_rules.split("\n")
        )
        compact_rules = defaultdict(list)

        for i, j in expanded_rules:
            compact_rules[j].append(i)
        
        updates = [
           [int(j) for j in i.split(",")] for i in raw_updates.split()
        ]
        return compact_rules, updates
            
if __name__ == "__main__":
    print(parse_input())