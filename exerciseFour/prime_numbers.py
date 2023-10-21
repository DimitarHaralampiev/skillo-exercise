def is_prime(num):
    return num % 2 == 0 and num >= 2


prime_numbers = {num for num in range(2, 100) if is_prime(num)}
print(prime_numbers)