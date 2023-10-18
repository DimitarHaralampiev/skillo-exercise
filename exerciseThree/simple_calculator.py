def simple_calculator(first_num, second_num, operator):
    operator_functions = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else 'Division by zero error'
    }

    if operator not in operator_functions:
        return 'Incorrect operator'

    return operator_functions[operator](first_num, second_num)


op = input('Please enter operator.Possible operators (+, -, *, /) ')
number_one = float(input('Please enter first Number '))
number_two = float(input('Please enter second Number '))

while op != 'Stop':
    print(f'{number_one} {op} {number_two} = {simple_calculator(number_one, number_two, op)}')
    op = input('Please enter operator.Possible operators (+, -, *, /) ')
