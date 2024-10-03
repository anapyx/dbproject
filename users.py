class User:
    def __init__(self, username):
        self.username = username

    def display_menu(self):
        raise NotImplementedError("Subclasses should implement this method")

class Admin(User):
    def display_menu(self):
        print("Admin Menu:")
        print("1. Add User")
        print("2. Remove User")
        print("3. View Logs")
        print("4. Exit")

class Client(User):
    def display_menu(self):
        print("Client Menu:")
        print("1. Edit Content")
        print("2. View Content")
        print("3. Exit")

class Viewer(User):
    def display_menu(self):
        print("Viewer Menu:")
        print("1. View Content")
        print("2. Exit")

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def display_menus(self):
        for user in self.users:
            print(f"\nMenu for {user.username}:")
            user.display_menu()

if __name__ == "__main__":
    admin = Admin("admin_user")
    client = Client("client_user")
    viewer = Viewer("viewer_user")

    manager = UserManager()
    manager.add_user(admin)
    manager.add_user(client)
    manager.add_user(viewer)

    manager.display_menus()