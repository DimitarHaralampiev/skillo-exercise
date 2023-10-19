class ShoppingCart:
    def __init__(self):
        # Initialize a dictionary to store shopping carts for different customers.
        self.shopping_carts = {}

    def add_item(self, customer_id, item, price, quantity):

        # Create or get the customer's cart and update the item information.
        cart = self.shopping_carts.setdefault(customer_id, {})
        item_info = cart.setdefault(item, {'price': price, 'quantity': 0})
        item_info['quantity'] += quantity

    def remove_item(self, customer_id, item):

        # Try to remove the specified item from the customer's cart.
        cart = self.shopping_carts.get(customer_id)
        if item in cart:
            return f'{cart.pop(item)} was deleted'
        return f'{item} does not in shopping cart.'

    def calculate_total(self, customer_id):

        # Calculate the total price for items in the customer's cart.
        cart = self.shopping_carts.get(customer_id)
        total_price = sum(item_info['price'] * item_info['quantity'] for item_info in cart.values())
        return f'Total price for {customer_id}\'s cart: {total_price:.2f}lv.'

    def display_cart(self, customer_id):
        if customer_id not in self.shopping_carts:
            return f'{customer_id} does not in shopping cart.'

        # Get the customer's cart and display its contents.
        cart = self.shopping_carts.get(customer_id)
        if not cart:
            return f'{customer_id}\'s cart is empty.'

        output = [f'{customer_id} Shopping Cart:']
        for item, item_info in cart.items():

            # Calculate the total price for each item and format it with 2 decimal places.
            output.append(
                f'{item}: {item_info["quantity"]} x {item_info["price"]}lv = {item_info["price"] * item_info["quantity"]:.2f}lv')
        output.append(self.calculate_total(customer_id))
        return '\n'.join(output)


shopping_cart = ShoppingCart()

choice = input('Enter your choice (Add/Remove/Display/Stop): ')

while choice != 'Stop':

    if choice == 'Add':
        customer_id = input('Enter customer ID: ')
        item = input('Enter item name: ')
        try:
            price = float(input('Enter item price: '))
            quantity = float(input('Enter quantity '))
            shopping_cart.add_item(customer_id, item, price, quantity)
        except ValueError:
            print('Invalid type price(number). Please enter a valid price(number).')
    elif choice == 'Remove':
        customer_id = input('Enter customer ID: ')
        item = input('Enter item to remove: ')
        print(shopping_cart.remove_item(customer_id, item))
    elif choice == 'Display':
        customer_id = input('Enter customer ID: ')
        print(shopping_cart.display_cart(customer_id))
    else:
        print('Invalid choice. Please choose Add, Remove, Display, or Stop.')

    choice = input('Enter your choice: ')

