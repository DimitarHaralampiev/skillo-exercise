class Rectangle:
    def __init__(self, length, width):
        # Initialize the Rectangle with length and width.
        self.__length = length  # Private attribute for length
        self.__width = width    # Private attribute for width

    def get_area(self):
        # Calculate and return the area of the rectangle.
        return self.width * self.length

    @property
    def length(self):
        # Getter for the length attribute.
        return self.__length

    @length.setter
    def length(self, value):
        # Setter for the length attribute.
        if value < 0:
            raise ValueError('Invalid length')
        self.__length = value

    @property
    def width(self):
        # Getter for the width attribute.
        return self.__width

    @width.setter
    def width(self, value):
        # Setter for the width attribute.
        if value < 0:
            raise ValueError('Invalid width')
        self.__width = value

    def __eq__(self, other):
        # Compare two rectangles based on their areas (equality).
        return self.get_area() == other.get_area()

    def __lt__(self, other):
        # Compare two rectangles based on their areas (less than).
        return self.get_area() < other.get_area()


# Create instances of Rectangle for testing
rectangle_one = Rectangle(4, 5)
rectangle_two = Rectangle(3, 6)
rectangle_three = Rectangle(4, 5)

print("Area Comparison:")
print(f"Rectangle one and Rectangle two have the same area: {rectangle_one == rectangle_two}")
print(f"Rectangle one and Rectangle three have the same area: {rectangle_one == rectangle_three}")

print(f"Rectangle one has a smaller perimeter than Rectangle two: {rectangle_one > rectangle_two}")
print(f"Rectangle three has a smaller perimeter than Rectangle one: {rectangle_three < rectangle_one}")