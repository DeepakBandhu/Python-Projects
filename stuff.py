#Parent
class User:
    name = "Deepak"
    email = "deepakbandhu12@gmail.com"
    password = "123423463"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")


#Child class employee
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "619798"

    #Same method as parent "user" except its using pin istead if password

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if(entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect")

#The other class
class Buyer(User):
    name = "Costco"
    location = "Sacramento"
    buyerId = "9090909090"


    def getLoginInfo(self):
        entry_name = input("Enter your stores name: ")
        entry_location = input("Enter your stores location: ")
        entry_buyerId = input("Enter your Buyer ID: ")
        if(entry_location == self.location and entry_buyerId == self.buyerId):
            print("Welcome back, {}!".format(entry_name))

if __name__ == "__main__":
    store = Buyer()
    store.getLoginInfo()
    
    manager = Employee()
    manager.getLoginInfo()

    
