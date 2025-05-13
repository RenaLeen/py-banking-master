from balance_inquiry import BalanceInquiry

def main():
    balance_inquiry = BalanceInquiry()

    balance_inquiry.add_transaction('Deposit', 500.00, 'Salary')
    balance_inquiry.add_transaction('Withdrawal', 200.00, 'ATM withdrawal')
    balance_inquiry.add_transaction('Transfer', 300.00, 'Transferred to savings')

    balance_inquiry.display_balance()
    balance_inquiry.display_transaction_history()

if __name__ == "__main__":
    main()
