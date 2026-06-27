class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(f"{self.book_id:<5}{self.title:<25}{self.author:<20}{status}")


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self):
        book_id = input("Enter Book ID: ")

        if book_id in self.books:
            print("Book ID already exists.")
            return

        title = input("Enter Title: ")
        author = input("Enter Author: ")

        self.books[book_id] = Book(book_id, title, author)
        print("Book added successfully.")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        print("-" * 70)
        print(f"{'ID':<5}{'Title':<25}{'Author':<20}Status")
        print("-" * 70)

        for book in self.books.values():
            book.display()

        print("-" * 70)

    def search_book(self):
        keyword = input("Enter title or author: ").lower()

        found = False

        print("-" * 70)
        print(f"{'ID':<5}{'Title':<25}{'Author':<20}Status")
        print("-" * 70)

        for book in self.books.values():
            if keyword in book.title.lower() or keyword in book.author.lower():
                book.display()
                found = True

        if not found:
            print("No matching books found.")

        print("-" * 70)

    def issue_book(self):
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]

        if not book.available:
            print("Book already issued.")
            return

        book.available = False
        print("Book issued successfully.")

    def return_book(self):
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]

        if book.available:
            print("Book is already available.")
            return

        book.available = True
        print("Book returned successfully.")

    def delete_book(self):
        book_id = input("Enter Book ID: ")

        if book_id in self.books:
            del self.books[book_id]
            print("Book deleted.")
        else:
            print("Book not found.")

    def update_book(self):
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]

        title = input(f"New title ({book.title}): ")
        author = input(f"New author ({book.author}): ")

        if title.strip():
            book.title = title

        if author.strip():
            book.author = author

        print("Book updated successfully.")

    def statistics(self):
        total = len(self.books)
        available = 0
        issued = 0

        for book in self.books.values():
            if book.available:
                available += 1
            else:
                issued += 1

        print("\nLibrary Statistics")
        print("------------------")
        print("Total Books :", total)
        print("Available   :", available)
        print("Issued      :", issued)

    def preload(self):
        self.books["101"] = Book("101", "Python Basics", "John")
        self.books["102"] = Book("102", "Flask Guide", "David")
        self.books["103"] = Book("103", "AWS Cloud", "Smith")
        self.books["104"] = Book("104", "Docker Deep Dive", "Nigel")
        self.books["105"] = Book("105", "Git Essentials", "Scott")


def menu():
    print("\n" + "=" * 45)
    print("        LIBRARY MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Update Book")
    print("7. Delete Book")
    print("8. Statistics")
    print("9. Exit")
    print("=" * 45)


def main():
    library = Library()
    library.preload()

    while True:
        menu()

        choice = input("Enter choice: ")

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            library.search_book()

        elif choice == "4":
            library.issue_book()

        elif choice == "5":
            library.return_book()

        elif choice == "6":
            library.update_book()

        elif choice == "7":
            library.delete_book()

        elif choice == "8":
            library.statistics()

        elif choice == "9":
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()