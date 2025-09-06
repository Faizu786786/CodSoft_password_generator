import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number for length!")
        return
    
    characters = ""
    if var_letters.get():
        characters += string.ascii_letters
    if var_digits.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("No Characters Selected", "Please select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x300")

# Password Length
length_label = tk.Label(root, text="Password Length:", font=("Arial", 12))
length_label.pack(pady=5)
length_entry = tk.Entry(root, width=10, font=("Arial", 14))
length_entry.pack(pady=5)
length_entry.insert(0, "12")  # Default length

# Character Type Options
var_letters = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

letters_check = tk.Checkbutton(root, text="Include Letters", variable=var_letters)
letters_check.pack()
digits_check = tk.Checkbutton(root, text="Include Numbers", variable=var_digits)
digits_check.pack()
symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=var_symbols)
symbols_check.pack()

# Label and Entry to display password
label = tk.Label(root, text="Generated Password:", font=("Arial", 12))
label.pack(pady=10)
password_entry = tk.Entry(root, width=30, font=("Arial", 14))
password_entry.pack(pady=5)

# Buttons
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white")
generate_button.pack(pady=5)
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="blue", fg="white")
copy_button.pack(pady=5)

# Run the application
root.mainloop()