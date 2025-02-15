import requests

def fetch_metadata(isbn):
    """
    Fetches metadata for a book given its ISBN using the Google Books API.

    Args:
        isbn (str): The ISBN of the book to fetch metadata for.

    Returns:
        dict: A dictionary containing the book's metadata, including:
            - Title (str): The title of the book.
            - Author (str): The author(s) of the book.
            - Genre (str): The genre(s) of the book.
            - Publisher (str): The publisher of the book.
            - Year (str): The publication year of the book.
            - Description (str): A description of the book.
        None: If the metadata could not be fetched or the book was not found.
    """
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "items" in data and len(data["items"]) > 0:
            volume_info = data["items"][0]["volumeInfo"]

            return {
                "Title": volume_info.get("title", "Unknown"),
                "Author": ", ".join(volume_info.get("authors", ["Unknown"])),
                "Genre": ", ".join(volume_info.get("categories", ["Unknown"])),
                "Publisher": volume_info.get("publisher", "Unknown"),
                "Year": volume_info.get("publishedDate", "Unknown"),
                "Description": volume_info.get("description", "")
            }

    return None