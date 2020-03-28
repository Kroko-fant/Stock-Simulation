class IllegalAccessException(Exception):
    pass


class Stock:

    def __init__(self, name, price, stype):
        self.name = name
        self.price = price
        while -1 > stype or 1 > stype:
            stype = stype / 10
        self._stype = stype

    def set_name(self, name):
        raise IllegalAccessException("Du kannst dieses Attribut nicht verändern!")

    def set_price(self, price):
        raise IllegalAccessException("Du kannst dieses Attribut nicht verändern!")

    def set_type(self, type):
        raise IllegalAccessException("Du kannst dieses Attribut nicht verändern!")

    def update_price(self, szenario):
        self.price = round(self.price * ((1 + szenario.getpercentage()) * self._stype), 2)

    def __str__(self) -> str:
        return f'{self.name}: {self.price}'
