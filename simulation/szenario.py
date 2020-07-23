import random as r


def rand_szenario():
    return Szenario(r.randint(-3, 4))


class Szenario:

    def __init__(self, name):
        name = int(name)
        self.name = name
        if name >= 3:
            self.value = r.randint(1, 4)
        elif name == 2:
            self.value = r.randint(1, 2)
        elif name == 1:
            self.value = r.randint(-1, 2)
        elif name == 0:
            self.value = 0
        elif name == -1:
            self.value = r.randint(-2, 1)
        elif name == -2:
            self.value = r.randint(-2, -1)
        elif name <= -3:
            self.value = r.randint(-4, -1)
        else:
            self.value = r.randint(-1, 1)

    def getpercentage(self):
        percentage = (r.randint(self.value - 1, self.value + 1) / 10000)
        if percentage < - 1:
            percentage = - 0.99
        return percentage

    def updateszenario(self):
        if self.name == -3:
            return Szenario(-3)
        if self.name == 3:
            return Szenario(3)
        fktint = r.randint(-100_000, 100_000)
        if fktint < -99_990:
            value = -4
        elif fktint < -99_900:
            value = -3
        elif fktint < -99_000:
            value = -2
        elif fktint < -90_000:
            value = -1
        elif fktint > 90_000:
            value = 1
        elif fktint > 99_000:
            value = 2
        elif fktint > 99_900:
            value = 3
        elif fktint > 99_990:
            value = 4
        else:
            value = 0
        return Szenario(value + self.name)
