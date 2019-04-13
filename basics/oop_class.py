class Account():

    def __init__(self,owner,balance=0):

        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amt):

        self.balance = self.balance + dep_amt
        print(f"Added {dep_amt} to the balance")

    def withdrawal(self,wd_amt):

        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print("Withdrawal accepted")
        else:
            print("Sorry not enough funds!")

    def __str__(self):
        return f"Owner: {self.owner} \nBalances: {self.balance}"


"""

Test:
a = Account("Sam",500)
a.owner
a.balance
print(a)
a.deposit(100)
a.withdrawal(600)

"""

        