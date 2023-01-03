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
def addtojson(variable):
    users.append(variable)
    users_json = json.dumps(users)
    file = open("users.txt", "w")
    file.write(users_json)
    file.close()

# Find the username or password
def findInfo(array, info, item): 
    for i in range(len(array)):
        if array[i][info] == item:
            return i
    return -1

# Login and register menu functions 
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

def login():
    usernameInput = input("Username: ")
    foundUser = findInfo(users, "username", usernameInput)
    foundUserLi.append(foundUser)
    if foundUser != -1:
        passwordInput = input("Password: ")
        foundPass = findInfo(users, "password", passwordInput)
        if foundPass != -1:
            print("Correct password")
            mainmenu()
        else: 
            print("Wrong Password! Try again!")
            login()
    else:
        print("No account found.")
        loginmenu()

def loginmenu():
    regOrLog = input("Would you like to register or login? ").lower() 
    if regOrLog == "login":
        login()
    elif regOrLog == "register":
        newuser = register()
        addtojson(newuser)
        mainmenu()

# Menu selection functions
def displayall():
    print("Deposit: ",users[foundUserLi[0]]["total"][0])
    print("Date: ",users[foundUserLi[0]]["total"][1],",",users[foundUserLi[0]]["total"][2])

def withdraw():
    pass

# Main menu functions 
def getMenuSelection():
    # Menu Options
    print(f"\n********MAIN MENU********")
    print("1. Display all trasactions")
    print("2. Withdraw money")
    print("3. Exit")
    return input("\nChoose an option please: ").lower()

def mainmenu():
    loop = True
    while loop:
        selection = getMenuSelection()

        if selection == "1" or selection == "display all trasactions":
            displayall() # all money, amount of money, when it was lost
        elif selection == "2" or selection == "withdraw money":
            withdraw()
        elif selection == "3" or selection == "exit":
            loop = False
            print("Bye!")
        
# Main Code Function
def main():
    loginmenu()

main()