class Human:

    leg_count = 4
    can_walk = True

    def get_description(self):
        return "This is human"

    def get_leg_count(self, count):
        self.leg_count = count



man = Human()
man.get_leg_count(2)
print(man.get_description())
print("\nHuman:", man.leg_count, "Legs")













