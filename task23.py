class User:

    __password = "passwprd"


    def get_password(self):
        return self.__password

class ActiveUser(User):

    def get_password(self):
        return "********"

user = ActiveUser()
print(user.get_password())