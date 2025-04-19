from utils import load_json, save_json

class Transaction:
    def __init__(self, type: str, date: str, amount: float):
        self.type = type
        self.date = date
        self.amount = amount

class TransactionService:
    transactions: list = load_json("transactions.json")

    def deposit(self, amount: float):
        transaction = Transaction("deposit", "today", amount)
        self.transactions.append(transaction.__dict__)
        save_json("transactions.json", self.transactions)

    def withdrawal(self, amount: float):
        transaction = Transaction("withdraw", "today", amount)
        self.transactions.append(transaction.__dict__)
        save_json("transactions.json", self.transactions)

    def display_transactions(self):
        for transaction in self.transactions:
            print(transaction)
