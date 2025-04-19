from utils import load_json, save_json

class Loan:
    def __init__(self, user_id: int, loan_id: int, status: str, balance: float):
        self.user_id = user_id
        self.loan_id = loan_id
        self.status = status
        self.balance = balance

class LoanService:
    loans: list = load_json("loans.json")
    
    def apply_for_loan(self, user_id: int, amount: float):
        loan_id = len(self.loans) + 1
        loan = Loan(user_id, loan_id, "pending", amount)
        self.loans.append(loan.__dict__)
        save_json("loans.json", self.loans)
    
    def collect_payment(self, loan_id: int, payment_amount: float):
        for loan in self.loans:
            if loan["loan_id"] == loan_id:
                loan["balance"] -= payment_amount
                save_json("loans.json", self.loans)
    
    def display_loans(self):
        for loan in self.loans:
            print(loan)
