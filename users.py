import pickle


class UserManagement:
    def __init__(self):
        self.users = self.load_users()

    def create_user(self, username, password):
        self.users[username] = password
        self.save_users()

    def authenticate_user(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        return False

    def save_users(self):
        with open("data/users.pickle", "wb") as file:
            pickle.dump(self.users, file)

    def load_users(self):
        try:
            with open("data/users.pickle", "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return {}
