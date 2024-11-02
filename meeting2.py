import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menambahkan angka atau operator ke layar kalkulator
def add_to_expression(value):
    current_text = display_var.get()
    new_text = current_text + str(value)
    display_var.set(new_text)

# Fungsi untuk menghitung hasil
def calculate():
    try:
        result = eval(display_var.get())  # Menghitung ekspresi
        display_var.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        display_var.set("")

# Fungsi untuk menghapus layar
def clear():
    display_var.set("")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("300x400")

# Variabel untuk menampilkan ekspresi
display_var = tk.StringVar()

# Entry untuk menampilkan ekspresi
display_entry = tk.Entry(root, textvariable=display_var, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
display_entry.grid(row=0, column=0, columnspan=4)

# Membuat tombol-tombol kalkulator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        tk.Button(root, text=button, width=10, height=3, command=calculate).grid(row=row, column=col, columnspan=2)
    elif button == "C":
        tk.Button(root, text=button, width=10, height=3, command=clear).grid(row=row, column=col, columnspan=2)
    else:
        tk.Button(root, text=button, width=5, height=3, command=lambda b=button: add_to_expression(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Menjalankan loop utama tkinter
root.mainloop()
