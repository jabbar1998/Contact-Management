from users import UserManagement
from contacts import Contact
import validators


def main():
    user_manager = UserManagement()
    while True:
        user_option = input("Enter 1 to create a new user, 2 to login, or 'q' to quit: ")
        if user_option == '1':
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            user_manager.create_user(username, password)
        elif user_option == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if user_manager.authenticate_user(username, password):
                contact_manager(username)
            else:
                print("Authentication failed. Please try again.")
        elif user_option.lower() == 'q':
            break
        else:
            print("Invalid option. Please try again.")


def contact_manager(username):
    contact = Contact(username)
    while True:
        print("""\nContact Management System
        1. Add a new contact
        2. Edit an existing contact
        3. Delete a contact
        4. View all contacts 
        5. Quit""")
        option = input("Enter your choice: ")
        if option == '1':
            name = input("Enter contact name: ")
            email = input("Enter contact email: ")
            if not validators.is_valid_email(email):
                raise "The email is incourret"
            phone = input("Enter contact phone: ")
            if not validators.is_valid_phone(phone):
                raise "The Phone Number is incourret"
            contact.add_contact(name, email, phone)
        elif option == '2':
            name = input("Enter the name of the contact to edit: ")
            new_name = input("Enter the new name: ")
            new_email = input("Enter the new email: ")
            new_phone = input("Enter the new phone: ")
            contact.edit_contact(name, new_name, new_email, new_phone)
        elif option == '3':
            name = input("Enter the name of the contact to delete: ")
            contact.delete_contact(name)
        elif option == '4':
            contact.view_contacts()
        elif option == '5':
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
