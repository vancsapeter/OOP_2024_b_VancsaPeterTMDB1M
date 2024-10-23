from AirLine import AirLine

class Flight(AirLine):  # Definiálja a járat alapvető attribútumait (járatszám, célállomás, jegyár).
    def __init__(self, name, number, destination, price):
        super().__init__(name)
        self.name = name
        self.number = number
        self.destination = destination
        self.price = price

    def get_number(self):
        return self.number

    def get_destination(self):
        return self.destination

    def get_price(self):
        return self.price