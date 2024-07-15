class Account:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account balance for {self.owner}: ${self.balance}")
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, owner, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, owner, initial_balance)
            print(f"Account created for {owner} with account number {account_number} and initial balance ${initial_balance}.")
        else:
            print("Account number already exists.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)



def main():
    my_bank = Bank()
    
    # Create some accounts
    my_bank.create_account(1001, "Alice", 500)
    my_bank.create_account(1002, "Bob", 1000)

    # Interact with the accounts
    account = my_bank.get_account(1001)
    if account:
        account.check_balance()
        account.deposit(200)
        account.withdraw(100)
        account.check_balance()

    account = my_bank.get_account(1002)
    if account:
        account.check_balance()
        account.deposit(500)
        account.withdraw(1500)  # Attempting to withdraw more than the balance
        account.check_balance()

if __name__ == "__main__":
    main()
