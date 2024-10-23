from Flight import Flight


class InternationalFlight(Flight):  # Nemzetközi járatokra vonatkozó osztály, magasabb jegyárakkal.
    def __init__(self, name, number, destination, price, tp="International"):
        super().__init__(name, number, destination, price)

        self.name=name
        self.type = tp
        self.number = number
        self.destination = destination
        self.price = price
    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_destination(self):
        return self.destination

    def get_price(self):
        return self.price
    def get_tipus(self):
        return self.type


    def set_name(self, name):
       self.name=name
       return self

    def set_number(self, number):
        self.number = number
        return self

    def set_destination(self, destination):
        self.destination = destination
        return self

    def set_price(self, price):
        self.price = price
        return self
    def set_tipus(self, tp):
        self.type = tp
        return self

