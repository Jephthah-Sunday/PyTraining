class Human:

    leg_count = 4
    gender = ""

    def get_gender(self):
        return "Unknown " + str(self.gender)


class Woman(Human):
    gender = "Female"


class Man(Human):
    gender = "Male"


human = Human()
print(human.get_gender())

man = Man()
print(man.get_gender())

woman = Woman()
print(woman.get_gender())
