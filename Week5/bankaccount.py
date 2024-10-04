'''

'''
class bankaccount:
    # Contructor
    def __init__(self, account_holder, acc_number):
        self.account_holder = account_holder
        self.balance = 0
        
    # Deposit moneyy
    def deposit(self, dep_amount):
        if (dep_amount > 0):
            self.balance += dep_amount
            print(f"Successfully Deposited ${dep_amount} into {self.account_holder}'s Account.")
            self.display_balance()
        else:
            print(f"${dep_amount} is not an acceptable amount.")
    
    # Withdraw moneyy
    def withdraw(self, amount):
        if(amount > 0):
            if(amount <= self.balance):
                self.balance -= amount
                print(f"Successfully Withdrawn ${amount} into {self.account_holder}'s Account.")
                self.display_balance()
            else:
                print(f"Insufficient Funds in {self.account_holder}'s Account.")
                
    # Display balance
    def display_balance(self):
        print(f"Current Balance for {self.account_holder}: ${self.balance}")
                   
                
if __name__ == "__main__":
    print("hello")