class User( ):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def show_user_details(self):
        print("")
        print("Personal details :")
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0

    def deposite(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print("account balance has been updated: ",self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if self.amount>self.balance:
            print("Insufficient funds || available balance ",self.balance)
        else:
            self.balance=self.balance-self.amount
            print("Account balance has been updated: ",self.balance)
    def view_balance(self):
        self.show_user_details()
        print("Your account balance ",self.balance)

johan=Bank("Om",20,"m")
johan.deposite(10000)
johan.withdraw(2999)
johan.show_user_details()
johan.view_balance()