import pandas as pd
import os

def update_excel(book_data):
    """
    Updates the Excel file with new book data.

    This function checks if the Excel file exists. If it does, it reads the existing data into a DataFrame.
    If it does not, it creates a new DataFrame with predefined columns. The new book data is then appended
    to the DataFrame, and the updated DataFrame is saved back to the Excel file.

    Args:
        book_data (dict): A dictionary containing book information with keys corresponding to the columns
                          ["Title", "Author", "Genre", "Publisher", "Year", "Description", "Location", "Category"].

    Returns:
        None
    """
    file_path = "data/library-database.xlsx"

    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
    else:
        df = pd.DataFrame(columns=["Title", "Author", "Genre", "Publisher", "Year", "Description", "Location", "Category"])

    df = pd.concat([df, pd.DataFrame([book_data])], ignore_index=True)
    df.to_excel(file_path, index=False)