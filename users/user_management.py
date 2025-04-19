# user_management.py
from account import handle_account_option  # Adjust import for account menu
from utils import clear_console

class User:
    def __init__(self, user_id: int, username: str, pin: str):
        self.user_id = user_id
        self.username = username
        self.pin = pin


class UserService:
    current_user: User | None = None
    
    def login(self):
        user_id = input("Enter your User ID: ")
        pin = input("Enter your PIN: ")
        
        # Simulate login validation (here you can add actual checks against stored data)
        # For simplicity, we assume any login is successful for now.
        self.current_user = User(user_id, "Test User", pin)
        print("Login successful!")

    def register(self):
        print("Registering new user...")
        user_id = input("Enter a new User ID: ")
        username = input("Enter your Username: ")
        pin = input("Enter your PIN: ")
        
        # Register the user (you could add logic to save this to a JSON file or database)
        self.current_user = User(user_id, username, pin)
        print(f"User {username} registered successfully!")

# Function that will be used in main.py to handle user input
def handle_user_option():
    user_service = UserService()
    
    EXIT, LOGIN, REGISTER = 0, 1, 2
    
    option = None
    while option != EXIT:
        print("Options:")
        print(f"\t{LOGIN} : Login")
        print(f"\t{REGISTER} : Register")
        print(f"\t{EXIT} : Exit")
        
        option = int(input("\n\tChoose an option: "))
        
        if option == LOGIN:
            user_service.login()
            if user_service.current_user:
                clear_console()
                handle_account_option()  # Now call the account management flow
        elif option == REGISTER:
            user_service.register()
        elif option == EXIT:
            print("Exiting...")
        else:
            print("Invalid option. Try again.")
