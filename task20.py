class Human:

    leg_count = 4
    gender = "Male"

    def get_gender(self):
        return "Unknown"


class Man(Human):
    gender = "Male"

human = Human()
print(human.get_gender())

man = Man()
print(man.gender)
