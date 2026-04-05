import tkinter as tk
import random
import string

# Generate password
def generate_password():
    length = length_entry.get()

    if not length.isdigit() or int(length) <= 0:
        result_label.config(text="❌ Enter valid number")
        return

    length = int(length)

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))

    result_var.set(password)

# Copy to clipboard
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())

# Main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x250")
root.resizable(False, False)

# Title
title = tk.Label(root, text="🔐 Password Generator", font=("Arial", 16))
title.pack(pady=10)

# Input
length_label = tk.Label(root, text="Enter Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Generate button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

# Result
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12))
result_label.pack(pady=10)

# Copy button
copy_btn = tk.Button(root, text="Copy", command=copy_password)
copy_btn.pack()

# Run app
root.mainloop()