
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


temp = input('Please enter temperature')

while temp != 'Stop':
    temp = float(temp)
    print(f'Convert temp from fahrenheit to celsius {fahrenheit_to_celsius(temp)}')
    print(f'Convert temp from celsius to fahrenheit {celsius_to_fahrenheit(temp)}')
    temp = input('Please enter temperature')
