from functions import *
def start_cli():
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
        print("_" * 40, end='\n\n')
        
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
                    print(f"\n> {folder}")
        
        elif choice == '7':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    start_cli()