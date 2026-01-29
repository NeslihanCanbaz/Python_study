class Customer():
    def __init__(self,name,surname,tc_identification,phone):
        self.name = name
        self.surname = surname
        self.tc_identification = tc_identification
        self.phone = phone

    def display_information(self):
        print("Customer Name: ", self.name)
        print("Customer Surname: ", self.surname)
        print("Customer Tc: ", self.tc_identification)
        print("Customer phone: ", self.phone)
        
class Account():
    def __init__(self,customer,account_number,balance):
        self.customer = customer
        self.account_number = account_number
        self.balance = balance

    def display_information(self):
        self.customer.display_information()

    def deposit(self,amount):
        self.balance += amount
        print("New balance: ",self.balance)

    def money_check(self,amount):
        if self.balance < amount:
            print("The transaction could not be completed, insufficient balance.")
        else:
            self.balance -= amount
            print("New balance: ",self.balance)

    def display_balance(self):
        print("Acount balance: ", self.balance)        



customer1 = Customer("Ahmet", "Yılmaz", "12345678901", "05551234567")

account1 = Account(customer1, "TR123456", 1000)

account1.deposit(500)
account1.money_check(200)
account1.display_balance()
account1.display_information()
account1.money_check(2000)
