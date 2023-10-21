def intersection(set_one, set_two):
    return set_one.intersection(set_two)


set_one = set([x for x in input('Please enter item ').split() if x != 'Stop'])
set_two = set([x for x in input('Please enter item ').split() if x != 'Stop'])
print(intersection(set_one, set_two))
