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