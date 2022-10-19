class Human:

    leg_count = 4
    gender = ""

    def get_gender(self):
        return "Unknown"


class Man(Human):
    gender = "Male"

human = Human()
print(human.get_gender())

man = Man()
print(man.get_gender())
