import keyboard
import tkinter as tk
from tkinter import simpledialog
import app

# Initialize the global variable `program`
program = None
ocrText = "ctrl+shift+a"
appendText = "ctrl+shift+z"

# Define the hotkey actions
def action1():
    if not program.menuIsChecked("ocr"):
        return
    program.ocrActivate()

def action2():
    if not program.menuIsChecked("append"):
        return
    program.addText()

# Function to initialize hotkeys
def initialize_hotkeys(pro):
    global program
    program = pro
    keyboard.add_hotkey('ctrl+shift+a', action1)
    keyboard.add_hotkey('ctrl+shift+z', action2)

# Function to create and show the hotkey editing window
def create_hotkey_window():
    def update_hotkey1():
        global ocrText
        new_hotkey = simpledialog.askstring("Input", "Enter new hotkey for OCR:")
        if new_hotkey:
            keyboard.remove_hotkey('ctrl+shift+a')
            keyboard.add_hotkey(new_hotkey, action1)
            ocrText = new_hotkey
            label1.config(text=f"OCR Hotkey: {new_hotkey}")

    def update_hotkey2():
        global appendText
        new_hotkey = simpledialog.askstring("Input", "Enter new hotkey for Append:")
        if new_hotkey:
            keyboard.remove_hotkey('ctrl+shift+z')
            keyboard.add_hotkey(new_hotkey, action2)
            appendText = new_hotkey
            label2.config(text=f"Append Hotkey: {new_hotkey}")

    # Create the main window
    window = tk.Tk()
    window.title("Edit Hotkeys")

    window.geometry("400x200")

    # Create labels and buttons for hotkey updates
    global ocrText
    global appendText
    label1 = tk.Label(window, text="OCR Hotkey: " + ocrText)
    label1.pack()
    button1 = tk.Button(window, text="Edit OCR Hotkey", command=update_hotkey1)
    button1.pack()

    label2 = tk.Label(window, text="Append Hotkey: " + appendText)
    label2.pack()
    button2 = tk.Button(window, text="Edit Append Hotkey", command=update_hotkey2)
    button2.pack()

    # Start the Tkinter event loop
    window.mainloop()

def main():
    # Initialize the application
    global program
    program = app.Ui_MainWindow()
    #initialize_hotkeys(program)
    #create_hotkey_window()

if __name__ == "__main__":
    main()