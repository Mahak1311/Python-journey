'''Create a BankAccount class with attributes account_number, balance and owner_name.
Add methods to deposit, withdraw and check balance.'''

class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = float(balance)
        self.owner_name = owner_name

    def deposit(self, amount):
        if(amount<0):
            print("Amount is in negative, Please enter positive amount")
        else:
            self.balance+=amount  

    def withdraw(self, amount):
        if(amount<0):
            print("Amount is in negative, Please enter positive amount") 

        elif(self.balance<amount):
            print("Not enough balance")  

        elif(self.balance<=0):
            print("The balance is in negative withdraw not possible")

        else:
            self.balance-=amount

    def check_balance(self):
        print(self.balance)   

acc_no = input("Enter account number: ")
owner = input("Enter owner name: ")
balance = float(input("Enter initial balance: "))

acc1 = BankAccount(acc_no, balance, owner)

while True:

    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        acc1.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        acc1.withdraw(amount)

    elif choice == "3":
        acc1.check_balance()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")