number = int(input('Please enter number'))

for num in range(1, number + 1):
    for num_patt in range(1, num + 1):
        print(num_patt, end='')
    print()