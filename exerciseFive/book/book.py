class Book:

    def __init__(self, author, title, pages):
        self.author = author
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f'Title: {self.title} - Author: {self.author}'


book_one = Book("To Kill a Mockingbird", "Harper Lee", 281)
book_two = Book("1984", "George Orwell", 328)
book_three = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)

print("Book Information:")
print(book_one)
print(f"Number of pages in {book_one}: {len(book_one)}")
print(book_two)
print(f"Number of pages in {book_two}: {len(book_two)}")
print(book_three)
print(f"Number of pages in {book_three}: {len(book_three)}")