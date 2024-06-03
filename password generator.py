import string
import random
from tkinter import *
from tkinter import messagebox
import sqlite3

with sqlite3.connect("users.db") as db:
    cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(Username TEXT NOT NULL, GeneratedPassword TEXT NOT NULL);")
db.commit()
db.close()

def generate_password():
    name = username_entry.get()
    leng = length_entry.get()

    if name == "":
        messagebox.showerror("Error", "Name cannot be empty")
        return

    if not name.isalpha():
        messagebox.showerror("Error", "Name must be a string")
        username_entry.delete(0, END)
        return

    try:
        length = int(leng)
    except ValueError:
        messagebox.showerror("Error", "Password length must be a number")
        length_entry.delete(0, END)
        return

    if length < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters long")
        return

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    chars = "@#%&()\"?!"
    numbers = string.digits

    u = random.randint(1, length - 3)
    l = random.randint(1, length - 2 - u)
    c = random.randint(1, length - 1 - u - l)
    n = length - u - l - c

    password = random.sample(upper, u) + random.sample(lower, l) + random.sample(chars, c) + random.sample(numbers, n)
    random.shuffle(password)
    gen_passwd = "".join(password)
    generated_password_entry.delete(0, END)
    generated_password_entry.insert(0, gen_passwd)

def accept_password():
    name = username_entry.get()
    password = generated_password_entry.get()
    if name and password:
        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users WHERE Username = ?", (name,))
            if cursor.fetchall():
                messagebox.showerror("Error", "This username already exists! Please use another username")
            else:
                cursor.execute("INSERT INTO users(Username, GeneratedPassword) VALUES(?, ?)", (name, password))
                db.commit()
                messagebox.showinfo("Success", "Password generated successfully")
    else:
        messagebox.showerror("Error", "Please generate a password first")

def reset_fields():
    username_entry.delete(0, END)
    length_entry.delete(0, END)
    generated_password_entry.delete(0, END)

root = Tk()
root.title('Password Generator')
root.geometry('400x300')
root.config(bg='#FF8000')
root.resizable(False, False)

Label(root, text="Password Generator", fg='darkblue', bg='#FF8000', font='Arial 20 bold').pack(pady=10)

Label(root, text="Enter User Name:", font='Arial 12', bg='#FF8000', fg='darkblue').pack(pady=5)
username_entry = Entry(root, font='Arial 12')
username_entry.pack(pady=5)

Label(root, text="Enter Password Length:", font='Arial 12', bg='#FF8000', fg='darkblue').pack(pady=5)
length_entry = Entry(root, font='Arial 12')
length_entry.pack(pady=5)

Button(root, text="Generate Password", font='Arial 12 bold', fg='white', bg='#007BFF', command=generate_password).pack(pady=10)

Label(root, text="Generated Password:", font='Arial 12', bg='#FF8000', fg='darkblue').pack(pady=5)
generated_password_entry = Entry(root, font='Arial 12', fg='#DC143C')
generated_password_entry.pack(pady=5)

Button(root, text="Accept", font='Arial 12 bold', fg='white', bg='#28A745', command=accept_password).pack(pady=10)
Button(root, text="Reset", font='Arial 12 bold', fg='white', bg='#DC3545', command=reset_fields).pack(pady=10)

root.mainloop()
