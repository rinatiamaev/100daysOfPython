from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# SAVE PASSWORD=============================
def save_pass():
    site = site_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        site:{
            "email" : email,
            "password" : password,
        }
    }
    if len(site) == 0 or len(password) == 0:
        messagebox.showinfo(title="uuuups", message=f"some fields is empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # Load existing data
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}  # If file is missing or empty, start with an empty dictionary

        data.update(new_data)

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

            site_entry.delete(0, END)
            pass_entry.delete(0, END)


# GENERATE PASSWORD=============================

def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password_out = "".join(password_list)
    pass_entry.insert(0, password_out)
    pyperclip.copy(password_out)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("ipass")
window.config(padx=50, pady=50, bg="white")


canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=2)


site_label = Label(text="Website:", bg="white")
site_label.grid(column=0, row=1, sticky="E")

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2, sticky="E")

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3, sticky="E")


site_entry = Entry(width=42)
site_entry.grid(row=1, column=1, columnspan=2)
site_entry.focus()

email_entry = Entry(width=42)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"your@mail.com")

pass_entry = Entry(width=23)
pass_entry.grid(row=3, column=1)


gen_pas_button = Button(text="Generate Password", command=gen_pass)  
gen_pas_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_pass)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
