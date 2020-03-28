import random as r


class Szenario:

    def __init__(self, value):
        self.value = value

    def getpercentage(self):
        percentage = (r.randint(self.value - 1, self.value + 1) / 10000)
        if percentage < - 1:
            percentage = 0.99
        return percentage

    def updateszenario(self, factor):
        return Szenario((r.randint(-1, 1) / 10000) * factor + self.value)
