import tkinter as tk
from tkinter import filedialog

# Global variable to keep track of the currently opened file
current_file_path = None

def open_file_explorer():
    global current_file_path
    # Use the existing root window for file dialog
    file_path = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    # Check if a file was selected
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                current_file_path = file_path  # Update the global variable
                return content
        except Exception as e:
            print(f"Error reading the file: {e}")
            return None
    else:
        return None

def save_file(content):
    global current_file_path
    # If there is an open file, save to it
    if current_file_path:
        try:
            with open(current_file_path, 'w') as file:
                file.write(content)
        except Exception as e:
            print(f"Error saving the file: {e}")
    else:
        # If no file is open, prompt the "Save As" dialog
        save_as_file_explorer(content)

def save_as_file_explorer(content):
    global current_file_path
    # Use the existing root window for file dialog
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    # Check if a file path was specified
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(content)
                current_file_path = file_path  # Update the global variable
        except Exception as e:
            print(f"Error saving the file: {e}")
    else:
        print("Save operation cancelled")

def main():
    global root
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    # Your main application code here
    # Example: open a file and print its content
    #content = open_file_explorer()
    #if content:
    #    print(content)

if __name__ == "__main__":
    main()