import tkinter as tk
from tkinter import messagebox, simpledialog, Scrollbar, Frame
from functions import list_folders, create_folder, add_link, remove_link, view_folder, open_folder_links


def start_gui():
    root = tk.Tk()
    root.title("Bookmark App")
    root.geometry("650x600")
    
    light_mode = {
        "bg": "#E9ECEF",
        "text_bg": "#FAFAFA",
        "text_fg": "#333333",
        "button_bg": "#5A67D8",
        "button_fg": "white",
        "label_fg": "#000000",
        "select_bg": "#5A67D8"
    }
    
    dark_mode = {
        "bg": "#1E1E1E",
        "text_bg": "#2D2D2D",
        "text_fg": "#D4D4D4",
        "button_bg": "#3A3A3A",
        "button_fg": "white",
        "label_fg": "white",
        "select_bg": "#5A67D8"
    }
    
    current_mode = light_mode
    
    def apply_theme(theme):
        root.configure(bg=theme["bg"])
        button_frame.configure(bg=theme["bg"])
        folder_frame.configure(bg=theme["bg"])
        log_frame.configure(bg=theme["bg"])
        
        for button in buttons:
            button.config(bg=theme["button_bg"], fg=theme["button_fg"], activebackground=theme["select_bg"])
        
        folder_label.config(bg=theme["bg"], fg=theme["label_fg"])
        log_label.config(bg=theme["bg"], fg=theme["label_fg"])
        
        folder_list.config(bg=theme["text_bg"], fg=theme["text_fg"], selectbackground=theme["select_bg"])
        text_field.config(bg=theme["text_bg"], fg=theme["text_fg"])

    def toggle_theme():
        nonlocal current_mode
        current_mode = dark_mode if current_mode == light_mode else light_mode
        apply_theme(current_mode)

    button_frame = Frame(root, bg=current_mode["bg"])
    button_frame.pack(pady=15)

    folder_frame = Frame(root, bg=current_mode["bg"])
    folder_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    log_frame = Frame(root, bg=current_mode["bg"])
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
            text_field.insert(tk.END, f"Folder '{name}' created.\n")

    def add_new_link():
        try:
            folder = folder_list.get(folder_list.curselection())
            link = simpledialog.askstring("Add Link", "Enter link to add:")
            if link:
                add_link(folder, link)
                messagebox.showinfo("Success", f"Link added to '{folder}'.")
                text_field.insert(tk.END, f"Link added to '{folder}': {link}\n")
        except tk.TclError:
            messagebox.showwarning("Warning", "Please select a folder first.")

    def remove_existing_link():
        try:
            folder = folder_list.get(folder_list.curselection())
            link = simpledialog.askstring("Remove Link", "Enter link to remove:")
            if link:
                remove_link(folder, link)
                messagebox.showinfo("Success", f"Link removed from '{folder}'.")
                text_field.insert(tk.END, f"Link removed from '{folder}': {link}\n")
        except tk.TclError:
            messagebox.showwarning("Warning", "Please select a folder first.")

    def view_links():
        try:
            folder = folder_list.get(folder_list.curselection())
            links = view_folder(folder)
            if links:
                messagebox.showinfo("Links", "\n".join(links))
                text_field.insert(tk.END, f"Links in '{folder}':\n" + "\n".join(links) + "\n")
            else:
                messagebox.showinfo("Links", "No links found in this folder.")
                text_field.insert(tk.END, f"No links found in '{folder}'.\n")
        except tk.TclError:
            messagebox.showwarning("Warning", "Please select a folder first.")

    def open_links():
        try:
            folder = folder_list.get(folder_list.curselection())
            open_folder_links(folder)
            messagebox.showinfo("Opening Links", f"Opening all links in '{folder}'.")
            text_field.insert(tk.END, f"Opening all links in '{folder}'.\n")
        except tk.TclError:
            messagebox.showwarning("Warning", "Please select a folder first.")

    button_options = {
        "padx": 10, "pady": 5, "relief": "flat",
        "bg": current_mode["button_bg"], "fg": current_mode["button_fg"], 
        "activebackground": current_mode["select_bg"]
    }

    buttons = [
        tk.Button(button_frame, text="Create Folder", command=create_new_folder, **button_options),
        tk.Button(button_frame, text="Add Link", command=add_new_link, **button_options),
        tk.Button(button_frame, text="Remove Link", command=remove_existing_link, **button_options),
        tk.Button(button_frame, text="View Links", command=view_links, **button_options),
        tk.Button(button_frame, text="Open Links", command=open_links, **button_options),
        tk.Button(button_frame, text="Toggle Theme", command=toggle_theme, **button_options)
    ]
    
    for btn in buttons:
        btn.pack(side=tk.LEFT, padx=5)

    folder_label = tk.Label(folder_frame, text="Current Folders:", font=("Segoe UI", 12, "bold"), bg=current_mode["bg"], fg=current_mode["label_fg"])
    folder_label.pack(anchor='w', padx=5)

    log_label = tk.Label(log_frame, text="Logs:", font=("Segoe UI", 12, "bold"), bg=current_mode["bg"], fg=current_mode["label_fg"])
    log_label.pack(anchor='w', padx=5)

    folder_list = tk.Listbox(folder_frame, bg=current_mode["text_bg"], fg=current_mode["text_fg"], selectbackground=current_mode["select_bg"], font=("Segoe UI", 10), bd=0)
    folder_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

    scrollbar = Scrollbar(folder_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    folder_list.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=folder_list.yview)

    text_field = tk.Text(log_frame, height=10, width=50, bg=current_mode["text_bg"], fg=current_mode["text_fg"], font=("Segoe UI", 9), bd=0)
    text_field.pack(pady=10, fill=tk.BOTH, expand=True, padx=5)

    refresh_folders()
    root.mainloop()

if __name__ == "__main__":
    start_gui()
