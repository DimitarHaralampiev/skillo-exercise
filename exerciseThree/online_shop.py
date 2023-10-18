class ShoppingCart:
    def __init__(self):
        self.shopping_carts = {}

    def add_item(self, customer_id, item, price):
        if customer_id in self.shopping_carts:
            self.shopping_carts[customer_id].append((item, price))
        else:
            self.shopping_carts[customer_id] = [(item, price)]

    def remove_item(self, customer_id, item):
        if customer_id in self.shopping_carts:
            shopping_cart = self.shopping_carts[customer_id]
            for i, (cart_item, price) in enumerate(shopping_cart):
                if cart_item == item:
                    shopping_cart.pop(i)
                    return f'Removed item {item}'
        return f'{customer_id} does not exist'

    def calculate_total(self, customer_id):
        if customer_id in self.shopping_carts:
            total_price = sum(item[1] for item in self.shopping_carts[customer_id])
            return f'Total price for {customer_id} cart: {total_price}lv.'
        return f'{customer_id} does not exist'

    def display_cart(self, customer_id):
        if customer_id in self.shopping_carts:
            shopping_cart = self.shopping_carts[customer_id]
            if not shopping_cart:
                print(f'{customer_id} cart is empty.')
            print(f'{customer_id} Shopping Cart:')
            for (item, price) in shopping_cart:
                print(f'{item}: {price}lv.')
            print(self.calculate_total(customer_id))
        else:
            print(f'{customer_id} does not exist')


shopping_cart = ShoppingCart()

choice = input('Enter your choice (Add/Remove/Display/Stop): ')

while choice != 'Stop':

    if choice == 'Add':
        customer_id = input('Enter customer ID: ')
        item = input('Enter item name: ')
        price = float(input('Enter item price: '))
        shopping_cart.add_item(customer_id, item, price)
    elif choice == 'Remove':
        customer_id = input('Enter customer ID: ')
        item = input('Enter item to remove: ')
        print(shopping_cart.remove_item(customer_id, item))
    elif choice == 'Display':
        customer_id = input('Enter customer ID: ')
        shopping_cart.display_cart(customer_id)
    else:
        print('Invalid choice. Please choose Add, Remove, Display, or Stop.')

    choice = input('Enter your choice: ')

