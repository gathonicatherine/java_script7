class Account:
    name="money"  
    def __init__(self,name,phone,credit_limit):
          self.name=name
          self.phone=phone
          self.balance=0
          self.credit=0
          self.credit_limit=credit_limit

    def deposit(self,amount):
        if amount<=0:
            return f"the amount must be greater than zero"
        else:    

            self.balance += amount
            return f"Hello {self.name} you have deposited {amount}"
        
    def show_balance(self):
        return f"Hello {self.name} your balance is {self.balance}"   
    def withdraw(self,amount):
        if amount>0:
            return f"Hello {self.name} you have withdrawed {amount} and your balance is {self.balance}"
        elif amount<=0:
            return f"Amount must be greater than zero"

        elif amount>self.balance:
            return f"Amount must be lesser that zero"
        else:         
            self.balance -= amount
            return f"{self.balance}"

            # return f"hello {self.name} you have withdrawed {amount}"
    # def show_balance(self):
    #     return f"Hello {self.name} you balance is {self.balance}" 
    def borrow(self,amount):
        if amount>self.loan_limit:
            print(f"The amount is greater than your limit")
        elif self.loan>0:
            print(f"clear your debt")
        else:
            self.loan+=1 
            self.balance+=amount
            return f"you have successfully borrowed the money"    