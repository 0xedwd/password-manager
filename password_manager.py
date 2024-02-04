import json
from tkinter import messagebox


class PasswordManager:
    def __init__(self, filepath="data.json"):
        self.filepath = filepath

    def dump_json(self, data):
        with open(self.filepath, "w") as data_file:
            json.dump(data, data_file, indent=4)

    def load_json(self):
        try:
            with open(self.filepath, "r") as data_file:
                return json.load(data_file)
        except FileNotFoundError:
            return {}

    def save(self, website, email, password):
        new_data = {website: {"email": email, "password": password}}

        if not all([website, email, password]):
            messagebox.showinfo(title="Error", message="Please make sure all fields are filled")
            return False

        data = self.load_json()
        data.update(new_data)
        self.dump_json(data)
        return True

    def find_password(self, website):
        data = self.load_json()
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            return True
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")
            return False
