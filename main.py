class Bankaccount:
    def __init__(self):
        self.balance = 0
        print("The Account is created")
    def deposit(self):
        amount = float(input("Enter the amount to be deposited :"))
        self.balance = self.balance + amount
        print("deposit successful %f" % self.balance)
    def withdraw(self):
        amount = float(input("Enter the amount to withdraw :"))
        if (self.balance >= amount):
            self.balance = self.balance - amount
            print("Withdraw successful, The balance is %f" % self.balance)
        else:
            print("Insufficient balance")
    def get_balance(self):
        print("Your account balance is %f" % self.balance)

acc = Bankaccount()
acc.deposit()
acc.withdraw()
acc.get_balance()