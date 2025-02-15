from book_manager import add_book_manual, fetch_and_add_book, add_from_file
def main():
    print("Welcome Pedro's Library Database!")
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