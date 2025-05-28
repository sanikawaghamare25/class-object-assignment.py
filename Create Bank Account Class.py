'''
5. Write a python program to Create Bank Account Class
'''
class Account:
Account_User=str(input("Enter user name:"))
Account_No=int(input("Enter the number:"))
balance=int(input("Enter the balance:"))

Account_Type=str(input("Enter the type of account:"))
status=str(input("Enter the status Account:"))
'''
Account_User="Sanika"
Account_No=120255223553
balance=1200
Account_Type="Savaing"
status="Active"'''
def diplay(self):
print(" Account_User:", self.Account_User)
print("Account_No:",self.Account_No)
print("Balance:",self.balance)
print("Account_Type:",self.Account_Type)
print("Acconut status:",self. status)
e=Account()
e.diplay()
