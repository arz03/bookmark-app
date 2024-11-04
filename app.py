import os
import webbrowser
from config import BOOKMARK_DIR

# Ensure BOOKMARK_DIR is specified in config.py
if not BOOKMARK_DIR:
    raise Exception("BOOKMARK_DIR must be set in config.py")

# Create the directory if it doesn't exist
os.makedirs(BOOKMARK_DIR, exist_ok=True)

def list_folders():
    """List all bookmark folders."""
    return [f.replace('.txt', '') for f in os.listdir(BOOKMARK_DIR) if f.endswith('.txt')]

def create_folder(name):
    """Create a new bookmark folder."""
    with open(os.path.join(BOOKMARK_DIR, f"{name}.txt"), 'w') as f:
        print(f"Bookmark folder '{name}' created.")

def add_link(folder, link):
    """Add a link to a specific folder."""
    with open(os.path.join(BOOKMARK_DIR, f"{folder}.txt"), 'a') as f:
        f.write(link + '\n')
        print(f"Link added to '{folder}'.")

def remove_link(folder, link):
    """Remove a link from a specific folder."""
    folder_path = os.path.join(BOOKMARK_DIR, f"{folder}.txt")
    with open(folder_path, 'r') as f:
        lines = f.readlines()
    with open(folder_path, 'w') as f:
        for line in lines:
            if line.strip() != link:
                f.write(line)
    print(f"Link removed from '{folder}' if it existed.")

def view_folder(folder):
    """View all links in a specific folder."""
    with open(os.path.join(BOOKMARK_DIR, f"{folder}.txt"), 'r') as f:
        links = [line.strip() for line in f if line.strip()]
    print(f"\nLinks in '{folder}':")
    for link in links:
        print(link)
    return links

def open_folder_links(folder):
    """Open all links in a specific folder in the default web browser."""
    links = view_folder(folder)
    print("\nOpening all links in your browser...")
    for link in links:
        webbrowser.open(link)

def select_folder():
    """Display folders and let user choose one by number."""
    folders = list_folders()
    if not folders:
        print("No folders available.")
        return None
    print("Available folders:")
    for i, folder in enumerate(folders, start=1):
        print(f"{i}. {folder}")
    try:
        choice = int(input("Select a folder by number: ")) - 1
        if 0 <= choice < len(folders):
            return folders[choice]
        else:
            print("Invalid choice.")
            return None
    except ValueError:
        print("Invalid input.")
        return None

def main():
    print("Welcome to the Bookmark App!")
    while True:
        print("\nMenu:")
        print("1. Create a new bookmark folder")
        print("2. Add a link to a folder")
        print("3. Remove a link from a folder")
        print("4. View links in a folder")
        print("5. Open all links in a folder")
        print("6. List all folders")
        print("7. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            folder = input("Enter folder name: ").strip()
            create_folder(folder)
        
        elif choice == '2':
            folder = select_folder()
            if folder:
                link = input("Enter link to add: ").strip()
                add_link(folder, link)
        
        elif choice == '3':
            folder = select_folder()
            if folder:
                link = input("Enter link to remove: ").strip()
                remove_link(folder, link)
        
        elif choice == '4':
            folder = select_folder()
            if folder:
                view_folder(folder)
        
        elif choice == '5':
            folder = select_folder()
            if folder:
                open_folder_links(folder)
        
        elif choice == '6':
            folders = list_folders()
            if not folders:
                print("No folders found.")
            else:
                print("Available folders:")
                for folder in folders:
                    print(folder)
        
        elif choice == '7':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
