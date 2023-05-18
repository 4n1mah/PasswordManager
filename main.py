from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for sym in range(randint(2, 4))]
    password_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list1 = password_letters + password_symbols + password_numbers

    shuffle(password_list1)

    password1 = "".join(password_list1)

    print(f"Your password is: {password1}")
    password_entry.insert(0, password1)
    pyperclip.copy(password1)
    notification = messagebox.showinfo("Copied", "Password copied")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email_username = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any of the fields empty")

    else:
        is_ok = messagebox.askokcancel(title='Confirm', message=f"These are the details entered:\n "
                                                                f"Email: {email_username}\n Password: {password}\n"
                                                                f"Is it okay to save?")

        if is_ok:

            data = open("Data", "a+")
            data.write(f'{website.capitalize()}: {email_username} / {password}\n')
            data.close()

            website_entry.delete(0, END)
            # email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'Sadielrojas08@gmail.com')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons

password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(row=3, column=2)
add_button = Button(text='Add', command=save)
add_button.config(width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
