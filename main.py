# Finance Management by Sana S

import json 

# DICTIONARY
# Users
# Save users using JSON
file = open("users.txt", "r")
user_from_file = file.read()
file.close()

users = json.loads(user_from_file)

# VARIABLES
foundUserLi = [ ]

# FUNCTIONS
# Save to JSON
def addtojson():
    users_json = json.dumps(users)
    file = open("users.txt", "w")
    file.write(users_json)
    file.close()

class Menu:
    def __init__(self):
        self.loop = True

    # Find users in JSON list
    def searchuser(self, whatuser):
        for i in range(len(users)):
            if users[i]["username"] == whatuser:
                return i
        return -1

    # Change the total in an account
    def changetotal(self, towhom, changemonth, changeyear, changetot):
        users[towhom]["total"][1] = changemonth
        users[towhom]["total"][2] = changeyear
        users[towhom]["total"][0] = changetot

    # Menu selection functions
    # Display Account Info
    def displayall(self):
        print("Deposit: ",users[foundUserLi[0]]["total"][0])
        print("Date: ",users[foundUserLi[0]]["total"][1],",",users[foundUserLi[0]]["total"][2])

    # Take out money and when it is occurring 
    def withdraw(self):
        withdrawalsum = input("How much money would you like to withdraw? ")
        if int(withdrawalsum) > int(users[foundUserLi[0]]["total"][0]):
            print("Withdrawal amount larger than account total. Withdrawal cannot be made.")
        else:
            withdrawalmonth = input("What month is this withdrawal occuring? ")
            withdrawalyear = input("What year is this withdrawal occuring? ")
            self.changetotal(foundUserLi[0], withdrawalmonth, withdrawalyear, int(users[foundUserLi[0]]["total"][0]) - int(withdrawalsum))
            print("Withdrawal Amount:",withdrawalsum)
            print("New Total:",users[foundUserLi[0]]["total"][0])
            print("Date of Transaction: ",users[foundUserLi[0]]["total"][1],",",users[foundUserLi[0]]["total"][2])
            addtojson()

    # Deposit money and when it is occurring 
    def deposit(self):
        depositsum = input("How much money would you like to deposit? ")
        depositmonth =input("What month is this withdrawal occuring? ")
        deposityear = input("What year is this withdrawal occuring? ")
        self.changetotal(foundUserLi[0], depositmonth, deposityear, int(users[foundUserLi[0]]["total"][0]) + int(depositsum))
        print("Deposit Amount:",depositsum)
        print("New Total:",users[foundUserLi[0]]["total"][0])
        print("Date of Transaction: ",users[foundUserLi[0]]["total"][1],",",users[foundUserLi[0]]["total"][2])
        addtojson()

    # Transfer money to a different account
    def transfer(self):
        transfersum = input("How much money would you like to transfer? ")
        if int(transfersum) > int(users[foundUserLi[0]]["total"][0]):
            print("Transfer amount too large.")
        else:
            # If the sum being transferred is smaller than the total account sum
            transfermonth = input("When is this transfer taking place? ")
            transferyear = input("What year is this transfer occurring? ")
            transferperson = input("Who are you transferring money to? ")
            index = self.searchuser(transferperson)
            # If the user is found, add money to their account, remove money from user account
            if index != -1:
                self.changetotal(index, transfermonth, transferyear, int(users[index]["total"][0]) + int(transfersum))
                users[foundUserLi[0]]["total"][1] = transfermonth
                users[foundUserLi[0]]["total"][2] = transferyear
                users[foundUserLi[0]]["total"][0] = int(users[foundUserLi[0]]["total"][0]) - int(transfersum)
                print("Transfer completed.")
                addtojson()
            else:
                print(index)
                print("User not found.")

    # Main menu functions 
    def getMenuSelection(self):
        # Menu Options Display
        print(f"\n********MAIN MENU********")
        print("1. Display all trasactions")
        print("2. Withdraw money")
        print("3. Deposit money")
        print("4. Transfer Money to Another User")
        print("5. Exit")
        return input("\nChoose an option please: ").lower()
    
    # Choosing a menu option
    def mainmenu(self):
        self.loop = True
        while self.loop:
            selection = self.getMenuSelection()

            if selection == "1" or selection == "display all trasactions":
                self.displayall() 
            elif selection == "2" or selection == "withdraw money":
                self.withdraw()
            elif selection == "3" or selection == "deposit money":
                self.deposit()
            elif selection == "4" or selection == "transfer money to another user":
                self.transfer()
            elif selection == "5" or selection == "exit":
                self.loop = False
                addtojson()
                print("Bye!")

menu = Menu()

# Find the username or password
def findInfo(array, info, item): 
    for i in range(len(array)):
        if array[i][info] == item:
            return i
    return -1

# Login and register menu functions 
# Register Function
def register():
    username = input("\nWhat would you like your username to be? ")
    password = input("What would you like your password to be? ")
    depositsum = input("How much money is your account starting with? ")
    depositmonth = input("What month is it? ")
    deposityear = input("What year is it? ")
    firstdep = [depositsum, depositmonth, deposityear]
    return {
        "username": username,
        "password": password,
        "total": firstdep
    }

# Login Function 
def login():
    usernameInput = input("Username: ")
    foundUser = findInfo(users, "username", usernameInput)
    foundUserLi.append(foundUser)
    if foundUser != -1:
        passwordInput = input("Password: ")
        foundPass = findInfo(users, "password", passwordInput)
        if foundPass != -1:
            print("Correct password")
            menu.mainmenu()
        else: 
            print("Wrong Password!")
            loginmenu()
    else:
        print("No account found.")
        loginmenu()

# Starting Menu : Login or Register Screen
def loginmenu():
    regOrLog = input("Would you like to register or login? ").lower() 
    if regOrLog == "login":
        login()
    elif regOrLog == "register":
        newuser = register()
        users.append(newuser)
        addtojson()
        print("Please confirm username and password.")
        login() 
        menu.mainmenu()
        
# Main Code Function
def main():
    loginmenu()

main()
