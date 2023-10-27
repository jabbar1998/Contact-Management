import pickle
class Contact:
    def __init__(self, username):
        self.username = username
        try:
            with open(f"data/{username}_contacts.pickle", "rb") as file:
                self.contacts = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.contacts = []

    def add_contact(self, name, email, phone):
        contact_info = {"name": name, "email": email, "phone": phone}
        self.contacts.append(contact_info)
        self.save_contacts()


    def edit_contact(self, old_name, new_name, new_email, new_phone):
        if old_name in self.contacts:
            for contact in self.contacts:
                if contact["name"] == old_name:
                    contact["name"] = new_name
                    contact["email"] = new_email
                    contact["phone"] = new_phone
                    break
            self.save_contacts()
        else:
            print(f"{old_name} is not in your contacts")


    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact["name"] != name]
        self.save_contacts()

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}")

    def save_contacts(self):
        with open(f"data/{self.username}_contacts.pickle", "wb") as file:
            pickle.dump(self.contacts, file)







