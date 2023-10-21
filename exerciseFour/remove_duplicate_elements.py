def remove_duplicate_elements(lst_elements):
    return set(lst_elements)


lst_elements = [x for x in input('Please enter item ').split() if x != 'Stop']
print(remove_duplicate_elements(lst_elements))