from excel_manager import update_excel
from api_handler import fetch_metadata

def add_book_manual(title, author, category, location):
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
    metadata = fetch_metadata(isbn)
    if metadata:
        metadata["Location"] = location
        metadata["Category"] = category
        update_excel(metadata)
        print("Book added successfully with metadata!")
    else:
        print("Failed to fetch metadata.")

def add_from_file(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            isbn, location, category = line.strip().split(',')
            fetch_and_add_book(isbn, location, category)