# Finance Management by Sana S

import json 

# DICTIONARY
# Users

# Save users using JSON
file = open("users.txt", "r")
user_from_file = file.read()
file.close()

users = json.loads(user_from_file)

def addhs(variable):
    users_json = json.dumps(variable)
    file = open("users.txt", "w")
    file.write(users_json)
    file.close()

print(users)
