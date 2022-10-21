import re

#name, number, email, password

#CRUDS
'''
C: Create
R: Read
U: Update
D: Delete
S: Save
'''
REGEX_CHECK_EMAIL = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

users:list = [
  {
    "id": 1,
    "name": "ryn",
    "number": "001122334455",
    "email": "ryn@exampel.test",
    "password": "abc12345"
  }
]

id:int = 1

user:dict = {
  "id": 0,
  "name": "",
  "number": "",
  "email": "",
  "password": ""
}

def resetUser() -> None:
  global user
  user = {
    "id": 0,
    "name": "",
    "number": "",
    "email": "",
    "password": ""
  }

def printUser(id:int) -> None:
  global users
  
  for user in users:
    if user["id"] == id:
      print(f"""
        Name: {user['name']}
        Number: {user['number']}
        Email: {user['email']}
        Password: {user['password']}
      """)
      return
  else:
    print("No User had been founded")
  
def readUsers() -> None:
    global users
  
    for user in users:
        print(f"""
            Name: {user['name']}
            Number: {user['number']}
            Email: {user['email']}
            Password: {user['password']}
        """, end="\n\n")

def checkInputs() -> None:
  global user, regexCheckEmail
  
  if not re.fullmatch("[a-zA-Z]", user['name']):
    while not re.findall("[a-zA-Z]", user['name']):
      user["name"] = input("Enter your name: ")
      
  if not re.fullmatch("\d", user["number"]):
    while not re.findall("\d", user["number"]):
      user["number"] = input("Enter your phone number: ")
  else:
    user["number"] = int(user["number"])

  if not re.fullmatch(REGEX_CHECK_EMAIL, user["email"]):
    while not re.fullmatch(REGEX_CHECK_EMAIL, user["email"]):
      user["email"] = input("Enter your email: ")

  if not re.fullmatch("([a-z]+)([A-Z]+)([0-9]+)", user["password"]):
    while not re.fullmatch("([a-z]+)([A-Z]+)([0-9]+)", user["password"]):
      user["password"] = input("Enter your password: ")
    
def createUser() -> None:
  global id, user, users
  id += 1
  user["id"] = id
  user["name"] = input("Enter your name: ")
  user["number"] = input("Enter your phone number: ")
  user["email"] = input("Enter your email: ")
  user["password"] = input("Enter your password: ")

  checkInputs()
  users.append(user)
  resetUser()
  printUser(id)
  
def updateUser() -> None:
    global users, user

    userId = input("Enter your id: ")
    
    for userLoop in users:
        if str(userLoop["id"]) == userId:
            user["name"] = input("Enter your name: ")
            user["number"] = input("Enter your phone number: ")
            user["email"] = input("Enter your email: ")
            user["password"] = input("Enter your password: ")

            checkInputs()

            userLoop["name"] = user["name"]
            userLoop["number"] = user["number"]
            userLoop["email"] = user["email"]
            userLoop["password"] = user["password"]

            resetUser()

            return
    else:
        print("No User had been founded")


def deleteUser() -> None:
    global users

    userId = input("Enter your id: ")
    
    for i in range(len(users)):
        if str(users[i]["id"]) == userId:
            users.pop(i)
            return
    else: 
        print("No change")

def checkChoice(choice:int) -> None:
    if choice == 1:
        createUser()
    elif choice == 2:
        readUsers()
    elif choice == 3:
        updateUser()
    elif choice == 4:
        deleteUser()

def main():
    while True:
        choice = input("Enter a choice: ")

        if not re.fullmatch('\d', choice):
            while not re.fullmatch('\d', choice):
                choice = input("Enter a choice: ")
        
        choice = int(choice)
        checkChoice(choice)  

      
if __name__ == "__main__":
  main()