#Original User Class Setup:
class User:	#the class name	
    def __init__(self, name, email): 
        self.name = name
        self.email = email 
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)
        return self
    def transfer_money(self, recipient, amount):
        self.account_balance -= amount
        recipient.account_balance += amount
        print("Recipient now has", recipient.account_balance)
        print("Sender now has", self.account_balance)
        return self

#Original BankAccount Class Setup:
class BankAccount:
    bank_name = "Frank Steglinski Capital International"
    all_accounts = []
    def __init__(self, int_rate, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    def display_account_info(self):
        print ("Balance:", self.balance)
        return self
    def yield_interest(self):
        self.balance = self.balance * (1 + self.int_rate)
        return self
    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum
    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

#Latest association between the two classes, per the previous lesson:
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print("Balance:", self.account.balance)
        return self
    def transfer_money(self, recipient, amount):
        self.account.balance -= amount
        recipient.account.balance += amount
        print("Recipient now has", recipient.account.balance)
        print("Sender now has", self.account.balance)
        return self

Frank = User("Frank Steglinski", "fjsteglinski@gmail.com")
Frank.make_deposit(100)

Isabelle = User("Isabelle Steglinski", "is@hotmail.com")

Frank.transfer_money(Isabelle, 50)
print(Frank.display_user_balance())
print(Isabelle.display_user_balance())

#How to allow a user to have multiple accounts;
#update methods so the user has to specify which account they are withdrawing or depositing to?