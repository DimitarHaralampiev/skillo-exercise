def is_subset(set_one, set_two):
    return set_one.issubset(set_two)


set_one = set([x for x in input('Please enter item ').split() if x != 'Stop'])
set_two = set([x for x in input('Please enter item ').split() if x != 'Stop'])
print(is_subset(set_one, set_two))