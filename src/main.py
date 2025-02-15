from book_manager import add_book_manual, fetch_and_add_book, add_from_file
def main():
    """
    Main function to interact with Users Library Database.

    This function provides a command-line interface with the following options:
    1. Add a book manually by entering the title, author, category, and location.
    2. Add a book by fetching metadata using the ISBN and specifying the location.
    3. Add books from a file by providing the file path.
    4. Exit the program.

    Usage:
    Run the script and follow the on-screen prompts to manage the library database.
    """
    print("Welcome to [Insert Name] Library Database!")
    while True:
        print("\nOptions:")
        print("1. Add a book manually")
        print("2. Add a book by fetching metadata")
        print("3. Add from a file")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            category = input("Enter the category: ")
            location = input("Enter the location: ")
            add_book_manual(title, author, category, location)
        elif choice == "2":
            isbn = input("Enter the ISBN: ")
            location = input("Enter the location: ")
            fetch_and_add_book(isbn, location)
        elif choice == "3":
            file_path = input("Enter the file path: ")
            add_from_file(file_path)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()