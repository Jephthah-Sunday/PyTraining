class Human:

    gender = "Male"
    skin_tone = "Chocolate"
    Height = "5.8ft"
    weight = "80"

    def get_human(self):
        return self.gender + "\n" + self.skin_tone + "\n" + self.Height

detail = Human()
print(detail.get_human())