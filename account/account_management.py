# accounts/account_management.py

import json
import os
from utils.utility import clear_console

ACCOUNTS_FILE = "data/accounts.json"

def load_accounts():
    if not os.path.exists(ACCOUNTS_FILE):
        return {}
    with open(ACCOUNTS_FILE, "r") as f:
        return json.load(f)

def save_accounts(accounts):
    with open(ACCOUNTS_FILE, "w") as f:
        json.dump(accounts, f, indent=4)

def handle_account_option(username):
    while True:
        clear_console()
        print(f"===== Account Management for {username} =====")
        print("1. View Account")
        print("2. Create Account")
        print("3. Delete Account")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_account(username)
        elif choice == "2":
            create_account(username)
        elif choice == "3":
            delete_account(username)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
            input("Press Enter to continue...")

def view_account(username):
    accounts = load_accounts()
    account = accounts.get(username)
    clear_console()
    if account:
        print("=== Account Info ===")
        for key, value in account.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No account found for this user.")
    input("\nPress Enter to return...")

def create_account(username):
    accounts = load_accounts()
    if username in accounts:
        print("Account already exists.")
    else:
        account_number = input("Enter new account number: ")
        balance = float(input("Enter initial balance: "))
        accounts[username] = {
            "account_number": account_number,
            "balance": balance
        }
        save_accounts(accounts)
        print("Account created successfully.")
    input("Press Enter to return...")

def delete_account(username):
    accounts = load_accounts()
    if username in accounts:
        confirm = input("Are you sure you want to delete your account? (yes/no): ").lower()
        if confirm == "yes":
            del accounts[username]
            save_accounts(accounts)
            print("Account deleted.")
        else:
            print("Deletion cancelled.")
    else:
        print("No account to delete.")
    input("Press Enter to return...")
