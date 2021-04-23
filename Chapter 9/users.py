class User:
    """a class for creating user profiles"""
    def __init__(self,firstName,lastName,userName,age,country,email,dateOfBirth,lastLogin):
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.age = age
        self.country = country
        self.email = email
        self.dateOfBirth = dateOfBirth
        self.lastLogin = lastLogin
        self.loginAttempts = 0

    def describe_user(self):
        #possibly upgrade this be more pythonic by looping through the attributes of the class
        print(f"***User Summary***")
        print(f"Username: {self.userName}")
        print(f"Name: {self.firstName} {self.lastName}")
        print(f"Email: {self.email}")
        print(f"Country: {self.country}")
        print(f"Date of Birth: {self.dateOfBirth}")
        print(f"Age: {self.age}")

    def greet_user(self):
        print(f"Hi {self.firstName}, welcome back! Your last login was {self.lastLogin}.")

    def incrementLoginAttempts(self):
        self.loginAttempts += 1
        print(f"You have attempted to login {newUser.loginAttempts} times.")

    def resetLoginAttempts(self):
        self.loginAttempts = 0



users = [("Robert","Brown","robbiecares","35","Germany","robbiecares@gmail.com","12/05/1985","29/06/2020")]

"""
for firstname,lastname,username,age,country,email,dateOfBirth,lastLogin in users:
    newUser = User(firstname,lastname,username,age,country,email,dateOfBirth,lastLogin)
    User.describe_user(newUser)
    User.greet_user(newUser)


newUser.incrementLoginAttempts()

newUser.incrementLoginAttempts()

newUser.incrementLoginAttempts()

newUser.resetLoginAttempts()

print(newUser.loginAttempts) -
"""

class Privileges:
    def __init__(self,privileges = ["can add post", "can delete post", "can ban user", "can unlock account"]):
        self.privileges = privileges

    def show_privileges(self):
        #TODO: add line that prints username
        print("***Privileges***")
        for priv in self.privileges:
            print(priv)


class Admin(User):
    """god user class"""
    def __init__(self,firstName,lastName,userName,age,country,email,dateOfBirth,lastLogin):
        super().__init__(firstName,lastName,userName,age,country,email,dateOfBirth,lastLogin)
        self.privileges = Privileges()

superuser = Admin("Robert","Brown","robbiecares","35","Germany","robbiecares@gmail.com","12/05/1985","29/06/2020",)


superuser.privileges.show_privileges()


