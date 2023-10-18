shopping_carts = {}


def add_item(customer_id, item, price):
    if customer_id in shopping_carts:
        shopping_carts[customer_id].append((item, price))
    else:
        shopping_carts[customer_id] = [(item, price)]


def remove_item(customer_id, item):
    if customer_id not in shopping_carts:
        return f'{customer_id} not found in {shopping_carts}.'

    shopping_cart = shopping_carts[customer_id]
    for i, (cart_item, price) in enumerate(shopping_cart):
        if cart_item == item:
            shopping_cart.pop(i)
            return f'Remove item {item}'


def calculate_total(customer_id):
    if customer_id not in shopping_carts:
        return f'{customer_id} does not have a shopping cart.'

    shopping_cart = shopping_carts[customer_id]
    total = sum(price for _, price in shopping_cart)
    return f'Total price for {customer_id} is cart: {total}lv.'


def display_cart(customer_id):
    if customer_id not in shopping_carts:
        raise ValueError(f'{customer_id} does not have a shopping cart.')

    shopping_cart = shopping_carts[customer_id]
    if not shopping_cart:
        raise ValueError(f'{customer_id} is cart is empty.')

    for (item, price) in shopping_cart:
        print(f'{item}: {price}lv.')


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
        remove_item(customer_id, item)
    elif choice == 'Calc':
        customer_id = input('Enter customer ID: ')
        total = calculate_total(customer_id)
        print(f'Total price for {customer_id} is cart: {total}lv.')
    elif choice == 'Display':
        customer_id = input('Enter customer ID: ')
        display_cart(customer_id)

    choice = input('Enter your choice: ')

