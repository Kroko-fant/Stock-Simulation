class IllegalAccessException(Exception):
    pass


class Stock:

    def __init__(self, name, price, count, stype):
        self.name = name
        self.count = count
        while -1 > stype or 1 < stype:
            stype = stype / 10
        self._stype = stype
        self.last_price = price

    def set_name(self, name):
        raise IllegalAccessException("Du kannst dieses Attribut nicht verändern!")

    def set_price(self, price):
        raise IllegalAccessException("Du kannst dieses Attribut nicht verändern!")

    def set_stype(self, stype):
        raise IllegalAccessException("Du kannst dieses Attribut nicht verändern!")

    def update(self, szenario):
        self.last_price = round(self.last_price * ((1 + szenario.getpercentage()) * self._stype), 2)

    def __str__(self) -> str:
        return f'{self.name}: {self.last_price}'

    def __eq__(self, other):
        return self.name == other if type(other == str) else self.name == other.name
