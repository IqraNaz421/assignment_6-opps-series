# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    # Class variable
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Call the class method to increment book count
        Book.increment_book_count()

    # Class method to increment the total books count
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Create instances of Book
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Access the total books count
print(f"Total books in library: {Book.total_books}")
print(f"Book 1: {book1.title} by {book1.author}")
print(f"Book 2: {book2.title} by {book2.author}")