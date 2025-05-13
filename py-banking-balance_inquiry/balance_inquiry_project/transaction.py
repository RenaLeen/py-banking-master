from datetime import datetime

class Transaction:
    def __init__(self, transaction_type, amount, description):
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            'transaction_type': self.transaction_type,
            'amount': self.amount,
            'description': self.description,
            'timestamp': self.timestamp
        }
