# Library Database Project

## Overview
The Library Database project provides a comprehensive solution for managing personal libraries, catering primarily to collections of comics, manga, and books. Designed as an open-source tool, it allows users to maintain a catalog of their collections, track book locations, and share recommendations. Users can manually add entries, use ISBN lookups via the Google Books API, or perform bulk imports from files. This project solves the problem of organizing and showcasing personal collections while offering a way to lend or share books effectively.

## Key Features
- **Customizable Excel Sheet**: Stores basic book information.
- **Multiple Import Options**:
  1. Manually adding book information.
  2. Using ISBN for book metadata retrieval.
  3. Bulk ISBN imports from a file.
- **Google Books API Integration**: Fetches metadata for books by ISBN.

## Technologies Used
- **Python**: Core programming language.
- **openpyxl**: Enables Excel writing and reading via pandas.
- **pandas**: Handles data manipulation and updates the Excel sheet.
- **requests**: Makes API calls to fetch book metadata.
- **Google Books API**: Provides metadata for ISBN lookups.

## Installation Instructions
1. Clone the repository and open it in your preferred IDE.
2. Set up a virtual Python environment.
   ```bash
   python -m venv env
   source env/bin/activate  # For Unix-based systems
   env\Scripts\activate    # For Windows
   ```
3. Install dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions
1. Run the application by executing:
   ```bash
   python src/main.py
   ```
2. Use the terminal to add books through:
   - Manual entry.
   - ISBN lookup.
   - Bulk ISBN imports from a file (line-separated entries, comma-separated values for ISBN, location, and category).
3. The code generates an Excel file in the `data/` folder. Subsequent additions update this file.

### Example Bulk File Format
Create a file named `books.txt` with the following format:
```
sampleisbn1, location1, category1
sampleisbn2, location2, category2
sampleisbn3, location3, category3
```
Example:
```
9780140449136, physical, book
9784091263640, physical, manga
9780307465351, digital, comic
```

## Project Structure
```
personal-library-database/
├── src/
│   ├── main.py            # Entry point for the application
│   ├── book_manager.py    # Handles book addition and metadata fetching
│   ├── excel_manager.py   # Handles reading and writing to Excel
│   └── api_handler.py     # Handles API requests and responses
├── data/
│   ├── books.xlsx         # Your Excel database (initially empty or with headers)
│   └── backups/           # Folder for backup copies of the database (planned feature)
├── requirements.txt       # List of dependencies
├── README.md              # Project overview and instructions
└── .gitignore             # Ignored files and directories
```

## API Integration
- Sends HTTP requests to the Google Books API with provided ISBNs.
- Formats API responses to optimize Excel sheet additions.

## Future Enhancements
1. **GUI Interface**: For a user-friendly experience and cleaner interaction.
2. **Backup Functionality**: Saves a copy of the database to prevent data loss.

## Contributing
Contributions are welcomed and appreciated! Feel free to fork the repository, make improvements, and submit pull requests.

## License
This project is licensed under the MIT License.


