class Human:
    def __init__(self, eyes):
        self.eyes = 2

    def eyes(self):
        return (print("i have {} eyes".format(self.eyes)))


class Male(Human):
    def __init__(self, name, eyes):
        super().__init__(eyes)
        self.name = name

male_1 = Male("Johnson", 2)
eyes = male_1.eyes()
print(eyes)
