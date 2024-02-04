from tkinter import Tk, Canvas, Label, Entry, Button, PhotoImage, END
import pyperclip
from password_generator import PasswordGenerator
from password_manager import PasswordManager

DEFAULT_EMAIL = "placeholder@email.com"


class PasswordUI:
    def __init__(self):
        self.password_entry = self.email_entry = self.website_entry = None
        self.logo_image = None
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50)
        self.password_manager = PasswordManager()

        self.setup_ui()

    def setup_ui(self):
        canvas = Canvas(height=200, width=200)
        self.logo_image = PhotoImage(file="logo.png")
        canvas.create_image(100, 100, image=self.logo_image)
        canvas.grid(row=0, column=1)
        # Labels
        Label(text="Website:").grid(row=1, column=0)
        Label(text="Email/Username:").grid(row=2, column=0)
        Label(text="Password:").grid(row=3, column=0)

        # Entries
        self.website_entry = Entry(width=21)
        self.website_entry.grid(row=1, column=1)
        self.website_entry.focus()
        self.email_entry = Entry(width=38)
        self.email_entry.grid(row=2, column=1, columnspan=2)
        self.email_entry.insert(END, DEFAULT_EMAIL)
        self.password_entry = Entry(width=21)
        self.password_entry.grid(row=3, column=1)

        # Buttons
        Button(text="Generate Password", command=self.generate_password).grid(row=3, column=2)
        Button(text="Add", width=36, command=self.save_password).grid(row=4, column=1, columnspan=2)
        Button(text="Search", width=13, command=self.find_password).grid(row=1, column=2, columnspan=2)

    def generate_password(self):
        password = PasswordGenerator.generate_password()
        self.password_entry.delete(0, END)
        self.password_entry.insert(END, password)
        pyperclip.copy(password)

    def save_password(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if self.password_manager.save(website, email, password):
            self.website_entry.delete(0, END)
            self.password_entry.delete(0, END)

    def find_password(self):
        website = self.website_entry.get()
        self.password_manager.find_password(website)

    def run(self):
        self.window.mainloop()
