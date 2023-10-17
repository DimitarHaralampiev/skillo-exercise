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


op = input('Please enter operator')
number_one = 5.5
number_two = 24
print(simple_calculator(number_one, number_two, op))
