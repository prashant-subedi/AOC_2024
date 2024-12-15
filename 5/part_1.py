
from parse_input import parse_input

rules, updates = parse_input()
sum = 0
for update in updates:
    invalid_page = set()
    for page in update:
        if page in invalid_page:
            break
        if page in rules:
            invalid_page.update(rules[page])
    else:
        sum += update[len(update)//2]
print(sum)