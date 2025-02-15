import requests

def fetch_metadata(isbn):
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