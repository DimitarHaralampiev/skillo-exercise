def even_number(lst_numbers):
    even = [x for x in lst_numbers if x % 2 == 0]
    return even


lst_numbers = [int(x) for x in input('Please enter number ').split() if x != 'Stop' and x.isdigit()]
print(even_number(lst_numbers))