from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT_NAME = "Copperplate Gothic Bold"
FONT_SIZE = 12
BG_COLOUR = "#000000"
FONT_COLOUR = "#fff"

# RANDOM PASSWORD GENERATOR/STORAGE MANAGER
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters =[choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# SAVES DATA INTO JSON FORMAT.
def save():

    entry_email = open("e-mail.txt", "r")
    content = entry_email.read()

    website = web_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": content,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Area Empty", message="Please make sure you have filled in all areas.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)

# SEARCHING AND RETRIEVING PASSWORD ALREADY IN JSON FILE
def find_password():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# SAVES MAIN EMAIL FOR REGULAR USE
def save_text():
   text_file = open("e-mail.txt", "w")
   text_file.write(email_entry.get(1.0, END))
   text_file.close()

# TKINTER UI SET UP
# CREATES TKINTER WINDOW
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20, background=BG_COLOUR)

# ADDS IMAGE TO TKINTER (USING GRID TO PLACE IT IN WINDOW)
canvas = Canvas(width=200, height=200, background=BG_COLOUR, highlightthickness=0)
logo_image = PhotoImage(file="filelogo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# SETTING UP AND PLACING LABELS
website_label = Label(text="Website:", font=(FONT_NAME, FONT_SIZE), width=20,
                         background=BG_COLOUR, foreground=FONT_COLOUR)
email_label = Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE), width=20,
                         background=BG_COLOUR, foreground=FONT_COLOUR)
password_label = Label(text="Password:", font=(FONT_NAME, FONT_SIZE), width=20,
                         background=BG_COLOUR, foreground=FONT_COLOUR)
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# SETTING UP AND PLACING BUTTONS
generate_button = Button(text="Generate Password", font=(FONT_NAME, FONT_SIZE, "bold"), width=20,
                         command=generate_password, background=BG_COLOUR, foreground=FONT_COLOUR)
add_button = Button(text="Add", font=(FONT_NAME, FONT_SIZE, "bold"), command=save, width=50,
                         background=BG_COLOUR, foreground=FONT_COLOUR)
update_email_button = Button(text="Update Email", font=(FONT_NAME, FONT_SIZE, "bold"), command=save_text, width=20,
                         background=BG_COLOUR, foreground=FONT_COLOUR)
search_button = Button(text="Search", font=(FONT_NAME, FONT_SIZE, "bold"), width=20, command=find_password,
                         background=BG_COLOUR, foreground=FONT_COLOUR)
generate_button.grid(column=2, row=3)
add_button.grid(column=0, row=4, columnspan=3)
search_button.grid(column=2, row=1)
update_email_button.grid(column=2, row=2)

# SETTING UP AND PLACING TEXT BOXES
web_entry = Entry(width=20)
email_entry = Text(width=20, height=1)
password_entry = Entry(width=20)
web_entry.grid(column=1, row=1)
# FOCUS ADDS CURSOR TO THIS ON ENTRY
web_entry.focus()
email_entry.grid(column=1, row=2)
password_entry.grid(column=1, row=3)
# PRE-ADDS EMAIL (0 PLACED AT START, END (CAPITALS) PLACES AT END)
entry_email = open("e-mail.txt", "r")
content = entry_email.read()
email_entry.insert("1.0", content)

# MAKES IT SO IT CAN RUN, MUST BE PLACED AT END!
window.mainloop()