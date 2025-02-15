from excel_manager import update_excel
from api_handler import fetch_metadata

def add_book_manual(title, author, category, location):
    """
    Adds a book to the library database manually with the given details.

    Args:
        title (str): The title of the book.
        author (str): The author of the book.
        category (str): The category of the book.
        location (str): The location of the book in the library.

    Returns:
        None
    """
    book_data = {
        "Title": title,
        "Author": author,
        "Genre": "",
        "Publisher": "",
        "Year": "",
        "Description": "",
        "Category": category,
        "Location": location,
    }
    update_excel(book_data)
    print("Book added successfully!")

def fetch_and_add_book(isbn, location, category):
    """
    Fetches metadata for a book using its ISBN, adds location and category information,
    and updates an Excel file with the complete metadata.

    Args:
        isbn (str): The ISBN of the book to fetch metadata for.
        location (str): The location where the book is stored.
        category (str): The category of the book.

    Returns:
        None
    """
    metadata = fetch_metadata(isbn)
    if metadata:
        metadata["Location"] = location
        metadata["Category"] = category
        update_excel(metadata)
        print("Book added successfully with metadata!")
    else:
        print("Failed to fetch metadata.")

def add_from_file(filepath):
    """
    Reads a file containing book details, fetches metadata for each book using its ISBN,
    and updates an Excel file with the complete metadata.

    Args:
        filepath (str): The path to the file containing book details. Each line in the file
                        should contain the ISBN, location, and category of a book, separated by commas.

    Returns:
        None
    """
    with open(filepath, 'r') as file:
        for line in file:
            isbn, location, category = line.strip().split(',')
            fetch_and_add_book(isbn, location, category)