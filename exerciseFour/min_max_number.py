def min_number(numbers):
    if not numbers:
        return None

    min_num = numbers[0]

    for num in numbers:
        if num < min_num:
            min_num = num

    return min_num


def max_number(numbers):
    if not numbers:
        return None

    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num


n = (4, 5, 33, -55, 34, 4, 2)
print(min_number(n))
print(max_number(n))
