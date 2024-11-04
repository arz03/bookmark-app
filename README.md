# Bookmark App

A simple Bookmark Management Application created by Arjun Sarje. This application allows users to create folders for bookmarks, add links, remove links, view links, and open all links in a folder.

## Use Cases

- **Create Bookmark Folders**: Organize your bookmarks by creating folders.
- **Add Links**: Easily add links to specific folders for quick access.
- **Remove Links**: Manage your bookmarks by removing links that are no longer needed.
- **View Links**: Check all links stored in a specific folder.
- **Open Links**: Open all links in a folder in your default web browser.
- **Switch Themes**: Toggle between light and dark themes for better visibility.

## Setup Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/bookmark-app.git
   cd bookmark-app
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. You can install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Application**:
   Rename `exampleconfig.py` to `config.py` and set the `BOOKMARK_DIR` variable to your desired directory for storing bookmarks:
   ```python
   BOOKMARK_DIR = "path/to/your/bookmarks"
   ```

4. **Run the Application**:
   You can run the GUI version of the application using:
   ```bash
   python run_gui.py
   ```
   Or, if you prefer the command line interface, use:
   ```bash
   python run_cli.py
   ```

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request. 

## License

This project is licensed under the MIT License.

Made by Arjun Sarje.
