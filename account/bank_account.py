from utils import load_json, save_json

counter = 0

class BankAccount:
    def __init__(self, user_id: int = None, account_type: str = "saving", balance: float = 0.0):
        global counter
        self.user_id = user_id if user_id else counter
        counter += 1
        self.type = account_type
        self.balance = balance

    def save_account(self):
        accounts_data = load_json("accounts.json")
        accounts_data[self.user_id] = {"type": self.type, "balance": self.balance}
        save_json("accounts.json", accounts_data)

    @staticmethod
    def load_all_accounts():
        return load_json("accounts.json")
