def sum_elements(arr):
    result = sum(arr) if arr else 'Empty list'
    return result


print(sum_elements([1, 2, 3, 4]))
print(sum_elements([0]))
print(sum_elements([]))
print(sum_elements([-1, 1]))
