import json
from account import Account
from transaction import Transaction
from datetime import datetime

class BalanceInquiry:
    def __init__(self, account_file='data/accounts.json', transaction_file='data/transactions.json'):
        self.account = Account(account_file)
        self.transaction_file = transaction_file
        self.transaction_data = self.load_transaction_data()

    def load_transaction_data(self):
        try:
            with open(self.transaction_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    
    def save_transaction_data(self):
        with open(self.transaction_file, 'w') as file:
            json.dump(self.transaction_data, file, indent=4)

    def add_transaction(self, transaction_type, amount, description):
        transaction = Transaction(transaction_type, amount, description)
        self.transaction_data.append(transaction.to_dict())
        self.save_transaction_data()

        if transaction_type == 'Deposit':
            self.account.update_balance(amount)
        elif transaction_type == 'Withdrawal':
            self.account.update_balance(-amount)
        elif transaction_type == 'Transfer':
            self.account.update_balance(-amount) 

    def display_balance(self):
        print(f"Current Balance: ₱{self.account.get_balance()}")

    def display_transaction_history(self):
        self.update_year_if_needed()
        
        print("\nTransaction History:")

        sorted_transactions = sorted(self.transaction_data, key=lambda x: x['timestamp'], reverse=True)

        deposits = [t for t in sorted_transactions if t['transaction_type'] == 'Deposit']
        withdrawals = [t for t in sorted_transactions if t['transaction_type'] == 'Withdrawal']
        transfers = [t for t in sorted_transactions if t['transaction_type'] == 'Transfer']

        if deposits:
            print("\nDeposits:")
            for t in deposits:
                print(f"{t['timestamp']} - Deposit: ₱{t['amount']} - {t['description']}")

        if withdrawals:
            print("\nWithdrawals:")
            for t in withdrawals:
                print(f"{t['timestamp']} - Withdrawal: ₱{t['amount']} - {t['description']}")

        if transfers:
            print("\nTransfers:")
            for t in transfers:
                print(f"{t['timestamp']} - Transfer: ₱{t['amount']} - {t['description']}")

    def update_year_if_needed(self):
        """Ensures that the year is updated in the transactions when necessary."""
        current_year = datetime.now().year
        for transaction in self.transaction_data:
            transaction_year = int(transaction['timestamp'].split('-')[0])
            if transaction_year != current_year:
  
                old_timestamp = transaction['timestamp']
                updated_timestamp = old_timestamp.replace(str(transaction_year), str(current_year), 1)
                transaction['timestamp'] = updated_timestamp
