def hash_list(input_list):
    # Convert the list into a tuple to make it hashable
    tuple_representation = tuple(input_list)
    # Calculate the hash of the tuple
    return hash(tuple_representation)


my_list = [1, 2, 3, 'yes']
hashed_value = hash_list(my_list)

print(f'Original list: {my_list}')
print(f'Hashed value: {hashed_value}')