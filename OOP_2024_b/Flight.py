from AirLine import AirLine

class Flight(AirLine):  # Definiálja a járat alapvető attribútumait (járatszám, célállomás, jegyár).
    def __init__(self, name, number, destination, price):
        super().__init__(name)
        self._name = name
        self._number = number
        self._destination = destination
        self._price = price

    def get_number(self):
        return self._number

    def get_destination(self):
        return self._destination

    def get_price(self):
        return self._price

    def set_number(self, number):
        self._number = number
        return self
    def set_destination(self, destination):
        self._destination = destination
        return self
    def set_price(self, price):
        self._price = price
        return self
