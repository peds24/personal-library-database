import pandas as pd
import os

def update_excel(book_data):
    file_path = "data/library-database.xlsx"

    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
    else:
        df = pd.DataFrame(columns=["Title", "Author", "Genre", "Publisher", "Year", "Description", "Location", "Category"])

    df = pd.concat([df, pd.DataFrame([book_data])], ignore_index=True)
    df.to_excel(file_path, index=False)