

# class Bank:
#     name="Money"
#     def __init__(self,name,phonenumber,account):
#         self.name=name
#         self.phonenumber=phonenumber
#         self.account=account

#     def safe(self):
#           return f"Hello{self.name} your phonenumber is {self.phonenumber} and you have an {self.account}"  
from datetime import datetime

class Account:
    name="money"  
    def __init__(self,name,phone,loan_limit):
          self.name=name
          self.phone=phone
          self.balance=0
          self.loan=0
          self.loan_limit=loan_limit
          self.transactions = []
          self.withdraws = []
          self.loans = 0
          self.repays = []
       
          

    def deposit(self,amount):
        try:
            10+amount
        except TypeError:
            return f"The amount must be in figures"    
        if amount<=0:

            return f"the amount must be greater than zero"
        else:    

            self.balance += amount
            transactions = {"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Deposit"
            }
            self.transactions.append(transactions)
            
            return f"Hello {self.name} you have deposited {amount}"
        
    def show_balance(self):
        return f"Hello {self.name} your balance is {self.balance}"   
    def withdraw(self,amount):
        try:
            10+amount
        except TypeError:
            return f"The amount must be in figures"  
        if amount>0:
            return f"Hello {self.name} you have withdrawed {amount} and your balance is {self.balance}"
        elif amount<=0:
            return f"Amount must be greater than zero"

        elif amount>self.balance:
            return f"Amount must be lesser that zero"
        else:         
            self.balance -= amount
            withdraws = {"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Withdraw"
            }
            self.withdraws.append(withdraws)
            
            return f"{self.balance}"

            # return f"hello {self.name} you have withdrawed {amount}"
    # def show_balance(self):
    #     return f"Hello {self.name} you balance is {self.balance}" 
    def borrow(self,amount):
        try:
            10+amount
        except TypeError:
            return f"The amount must be in figures"  
        if amount>self.loan_limit:
            print(f"The amount is greater than your limit")
        elif self.loan>0:
            print(f"clear your debt")
        else:
            self.loan+=1 
            self.balance+=amount
            loans = {"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Loan"
            }
            self.loans.append(loans)
            return f"you have successfully borrowed the money"
    def get_statement(self):
        for transaction in self.transactions:
            narration=transaction["narration"]
            amount=transaction["amount"]
            balance=transaction["balance"]
            time=transaction["time"]
            print(f" At this time{time.strftime('%D')}eheee {narration}Amount {amount} Balance {balance} {time}")
        for withdrawal in self.withdraws:
            narration=withdrawal["narration"]
            amount=withdrawal["amount"]
            balance=withdrawal["balance"]
            time=withdrawal["time"]
            print(f" At this time{time.strftime('%D')}eheee {narration}Amount {amount} Balance {balance} {time}")
        for loan in self.loans:
            narration=loan["narration"]
            amount=loan["amount"]
            balance=loan["balance"]
            time=loan["time"]
            print(f" At this time{time.strftime('%D')}eheee {narration}Amount {amount} Balance {balance} {time}") 
        for lipa in self.repays:
            narration=lipa["narration"]
            amount=lipa["amount"]
            balance=lipa["balance"]
            time=lipa["time"]
            print(f" At this time{time.strftime('%D')}eheee {narration}Amount {amount} Balance {balance} {time}")        

    def repay_loan(self,amount):
        try:
            10+amount
        except TypeError:
            return f"The amount must be in figures"  
        if amount<0:
            return f"The amount should be greater than zero"
        elif amount<self.loan:
            self.loan-=amount   
            return f"You hava paid {amount} thank you"
        else:
            difference=amount-self.loan
            self.balance+=difference
            repay = {"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Repay"
            }
            self.repays.append(repay)
            return f"You have fullly paid your {self.loan}Kshs loan and your balance is {self.balance} Thank you "
    def transfer(self,amount,account):
        try:
            10-amount
        except TypeError:
            return f"The amount send to must be in figures"
        fee=amount*0.05      
        if amount+fee>self.balance:
            return f"YOur balance is {self.balance} you need {amount+fee}"
        else:
            self.balance-=amount+fee
            account.deposit(amount)
            return f"Your balance is{self.balance}"

                
class MobileMoney(Account):
    def __init__(self,name,phone,serviceprovider):
       
       super().__init__(name,phone,loan_limit=30000000)
       self.serviceprovider=serviceprovider
       self.limit=30000000
    def BuyAirtime(self,amount):
       return f"hello {self.name} number {self.phone} you bought airtime worth {amount}"

   



    
