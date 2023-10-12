number = int(input('Please enter number'))

for num in range(2, number + 1):
    if (num % 2 != 0) or (num == 2):
        print('Prime')
    else:
        print('Not prime')