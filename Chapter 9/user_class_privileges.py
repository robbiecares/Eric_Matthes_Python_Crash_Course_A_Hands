import user_class
class Privileges:
    def __init__(self,privileges = ["can add post", "can delete post", "can ban user", "can unlock account"]):
        self.privileges = privileges

    def show_privileges(self):
        #TODO: add line that prints username
        print("***Privileges***")
        for priv in self.privileges:
            print(priv)


class Admin(user_class.User):
    """god user class"""
    def __init__(self,firstName,lastName,userName,age,country,email,dateOfBirth,lastLogin):
        super().__init__(firstName,lastName,userName,age,country,email,dateOfBirth,lastLogin)
        self.privileges = Privileges()
