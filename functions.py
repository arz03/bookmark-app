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
    if not links:
        print("No links found in this folder.")
    else:
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
