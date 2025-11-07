import random
class BankAccount:
    AccountNumbers=[]
    lastAccountNumbers=999
    def __init__(self,name,family,age,email,phoneNumber):
          
        BankAccount.lastAccountNumbers+=1
        AN=BankAccount.lastAccountNumbers
        self.AccountNumber=AN
        self.AccountNumbers.append(AN)
        
        self.name=name
        self.family=family
        self.age=age
        self.email=email
        self.phoneNumber=phoneNumber
        self.total=0
    
    def Display(self):
        print(40*"-")
        print("Hi",self.name,self.family,"\n","Total:",self.total)
        print(f"AccountNumber is:{self.AccountNumber}")

        print(40*"-")

    def Deposit(self):
        Amount=float(input("enter your deposit number:"))
        self.total+=Amount
    def Withdrawal(self):
        Amount=float(input("enter your Withdrawal number:"))
        if Amount<=self.total:
            self.total-=Amount
        else:print("you are lack of money")


def main():
    nima=BankAccount("nima","fakhimi",20,"n1384.fakhimi@gmail.com","09301275197")
    while True:
        nima.Display()
        choice=int(input("Choose your option:\n1-show your current total\n2-Deposit\n3-Withdrawal\n4-Exit\nyour choice: "))
        if choice==1:
            nima.Display()
        elif choice==2:
            nima.Deposit()
        elif choice==3:
            nima.Withdrawal()
        else:break

main()