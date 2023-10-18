# Global dictionary to store shopping carts
shopping_carts = {}


# Function to add items to the cart
def add_item(customer_id, item, price):
    # If the customer already has a cart, append the new item.
    # Otherwise, create a new cart with the item.
    if customer_id in shopping_carts:
        shopping_carts[customer_id].append((item, price))
    else:
        shopping_carts[customer_id] = [(item, price)]


# Function to remove items from the cart
def remove_item(customer_id, item):
    # Ensure the customer exists.
    check_customer(customer_id)

    # Get the customer's shopping cart.
    shopping_cart = shopping_carts[customer_id]

    # Search for the item to remove and remove it if found.
    shopping_cart = shopping_carts[customer_id]
    for i, (cart_item, price) in enumerate(shopping_cart):
        if cart_item == item:
            shopping_cart.pop(i)
            return f'Removed item {item}'


# Function to calculate the total price of items in the cart
def calculate_total(customer_id):
    # Ensure the customer exists.
    check_customer(customer_id)

    # Calculate the total price of items in the cart.
    total_price = sum(item[1] for item in shopping_carts[customer_id])
    return f'Total price for {customer_id} cart: {total_price}lv.'


# Function to display the contents of the cart
def display_cart(customer_id):
    # Ensure the customer exists.
    check_customer(customer_id)

    # Get the customer's shopping cart.
    shopping_cart = shopping_carts[customer_id]

    # Check if the cart is empty and print its contents.
    if not shopping_cart:
        print(f'{customer_id} cart is empty.')

    print(f'{customer_id} Shopping Cart:')
    for (item, price) in shopping_cart:
        print(f'{item}: {price}lv.')
    print(calculate_total(customer_id))


def check_customer(customer_id):
    if customer_id not in shopping_carts:
        raise ValueError(f'{customer_id} does not in shopping cart')


choice = input('Enter your choice: ')

while choice != 'Stop':

    if choice == 'Add':
        customer_id = input('Enter customer ID: ')
        item = input('Enter item name: ')
        price = float(input('Enter item price: '))
        add_item(customer_id, item, price)
    elif choice == 'Remove':
        customer_id = input('Enter customer ID: ')
        item = input('Enter item to remove: ')
        print(remove_item(customer_id, item))
    elif choice == 'Display':
        customer_id = input('Enter customer ID: ')
        display_cart(customer_id)

    choice = input('Enter your choice: ')

