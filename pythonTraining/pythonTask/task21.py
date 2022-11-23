class Human:

    leg_count = 4
    gender = ""

    def get_gender(self):
       return "Unknown"


class Woman(Human):
    gender = "Female"

    def get_gender(self):
       return self.gender


class Man(Human):
    gender = "Male"

    def get_gender(self):
       return self.gender


human = Human()
print("Human:", human.get_gender())

man = Man()
print("Man:", man.get_gender())

woman = Woman()
print("Man:", woman.get_gender())
