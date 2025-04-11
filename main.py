from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- CREATING PATHS TO MAKE A .EXE APP ------------------------------- #
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

logo_path = resource_path("logo.png")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(10, 12)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ''.join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_website():
    site = website_entry.get()
    return site
def get_email():
    email = email_entry.get()
    return email
def get_password():
    password = password_entry.get()
    return password


def set_details():
    # Get the user's Documents folder
    # documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
    # data_file_path = os.path.join(documents_folder, "_my_user_data.json")
    new_data = {
        get_website(): {
            "email": get_email(),
             "password": get_password()
        }
    }

    if len(get_website()) == 0 or len(get_email()) == 0 or len(get_password()) == 0:
        messagebox.showerror(title="Error", message="Please fill all fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
           with open("data.json", "w") as data_file:
               json.dump(new_data, data_file, indent=4)  # writes to a json file
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent = 4) #writes to a json file
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No stored data file found.")
    except json.decoder.JSONDecodeError:
        messagebox.showerror("Error", "Corrupt or Empty JSON file.")
    else:
        if get_website() in data:
                messagebox.showinfo(title=get_website(), message = f"Email: {get_email()}\nPassword: {data[get_website()]["password"]}")
        else:
            messagebox.showerror(title=get_website(), message="No details for the website exists.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock = PhotoImage(file=logo_path)
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", command=find_password, width=15)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "test@gmail.com")

password_label = Label(text = "Password")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=30, command=set_details)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()

