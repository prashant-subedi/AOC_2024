
from parse_input import parse_input

rules, updates = parse_input()

def is_update_valid(update):
    invalid_page = set()
    for page in update:
        if page in invalid_page:
            return False
        if page in rules:
            invalid_page.update(rules[page])
    return True

def fix_update(update):
    invalid_page = dict()
    for index, page in enumerate(update):
        if page in invalid_page:
            update[index], update[invalid_page[page]] =  update[invalid_page[page]], update[index]
        if page in rules:
            for i in rules[page]:
                invalid_page[i] = index
    return update

sum = 0
for update in updates:
    if not is_update_valid(update):
        while not is_update_valid(update):
            update = fix_update(update)
        sum+=update[len(update)//2]
print(sum)