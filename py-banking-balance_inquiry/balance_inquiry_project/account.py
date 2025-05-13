import json

class Account:
    def __init__(self, account_file='data/accounts.json'):
        self.account_file = account_file
        self.account_data = self.load_account_data()

    def load_account_data(self):
        try:
            with open(self.account_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {"balance": 0.0}

    def save_account_data(self):
        with open(self.account_file, 'w') as file:
            json.dump(self.account_data, file, indent=4)

    def update_balance(self, amount):
        self.account_data['balance'] += amount
        self.save_account_data()
        
    def get_balance(self):
        return self.account_data['balance']
