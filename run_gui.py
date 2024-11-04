import tkinter as tk
from tkinter import messagebox, simpledialog, Scrollbar, Frame
from functions import list_folders, create_folder, add_link, remove_link, view_folder, open_folder_links

def start_gui():
    root = tk.Tk()
    root.title("Bookmark App")
    root.geometry("600x600")  # Set the window size (width x height)

    # Frame for Buttons
    button_frame = Frame(root)
    button_frame.pack(pady=10)

    # Frame for Folder List
    folder_frame = Frame(root)
    folder_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    # Frame for Logs
    log_frame = Frame(root)
    log_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    def refresh_folders():
        folders = list_folders()
        folder_list.delete(0, tk.END)
        for folder in folders:
            folder_list.insert(tk.END, folder)

    def create_new_folder():
        name = simpledialog.askstring("Folder Name", "Enter folder name:")
        if name:
            create_folder(name)
            refresh_folders()
            messagebox.showinfo("Success", f"Folder '{name}' created.")
            text_field.insert(tk.END, f"Folder '{name}' created.\n")  # Log message

    def add_new_link():
        try:
            folder = folder_list.get(folder_list.curselection())  # Get selected folder from list
            link = simpledialog.askstring("Add Link", "Enter link to add:")
            if link:
                add_link(folder, link)
                messagebox.showinfo("Success", f"Link added to '{folder}'.")
                text_field.insert(tk.END, f"Link added to '{folder}': {link}\n")  # Log message
        except tk.TclError:
            messagebox.showwarning("Warning", "Please select a folder first.")

    def remove_existing_link():
        try:
            folder = folder_list.get(folder_list.curselection())  # Get selected folder from list
            link = simpledialog.askstring("Remove Link", "Enter link to remove:")
            if link:
                remove_link(folder, link)
                messagebox.showinfo("Success", f"Link removed from '{folder}'.")
                text_field.insert(tk.END, f"Link removed from '{folder}': {link}\n")  # Log message
        except tk.TclError:
            messagebox.showwarning("Warning", "Please select a folder first.")

    def view_links():
        try:
            folder = folder_list.get(folder_list.curselection())  # Get selected folder from list
            links = view_folder(folder)
            if links:
                messagebox.showinfo("Links", "\n".join(links))
                text_field.insert(tk.END, f"Links in '{folder}':\n" + "\n".join(links) + "\n")  # Log message
            else:
                messagebox.showinfo("Links", "No links found in this folder.")
                text_field.insert(tk.END, f"No links found in '{folder}'.\n")  # Log message
        except tk.TclError:
            messagebox.showwarning("Warning", "Please select a folder first.")

    def open_links():
        try:
            folder = folder_list.get(folder_list.curselection())  # Get selected folder from list
            open_folder_links(folder)
            messagebox.showinfo("Opening Links", f"Opening all links in '{folder}'.")
            text_field.insert(tk.END, f"Opening all links in '{folder}'.\n")  # Log message
        except tk.TclError:
            messagebox.showwarning("Warning", "Please select a folder first.")

    # Button Layout
    tk.Button(button_frame, text="Create Folder", command=create_new_folder).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Add Link", command=add_new_link).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Remove Link", command=remove_existing_link).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="View Links", command=view_links).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Open Links", command=open_links).pack(side=tk.LEFT, padx=5)

    # Label for Current Folders
    tk.Label(folder_frame, text="Current Folders:", font=("Arial", 12)).pack(anchor='w', padx=5)

    # Folder List with Scrollbar
    folder_list = tk.Listbox(folder_frame)
    folder_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = Scrollbar(folder_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    folder_list.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=folder_list.yview)

    # Label for Logs
    tk.Label(log_frame, text="Logs:", font=("Arial", 12)).pack(anchor='w', padx=5)

    text_field = tk.Text(log_frame, height=10, width=50)  # Create a Text widget for logging messages
    text_field.pack(pady=10, fill=tk.BOTH, expand=True)

    refresh_folders()  # Load folders on startup
    root.mainloop()

if __name__ == "__main__":
    start_gui()
