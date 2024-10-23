from Flight import Flight


class InternationalFlight(Flight):  # Nemzetközi járatokra vonatkozó osztály, magasabb jegyárakkal.
    def __init__(self, name, number, destination, price, tp="International"):
        super().__init__(name, number, destination, price)

        self._name=name
        self._tipus = tp
        self._number = number
        self._destination = destination
        self._price = price
    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    def get_destination(self):
        return self._destination

    def get_price(self):
        return self._price
    def get_tipus(self):
        return self._tipus


    def set_name(self, name):
       self._name=name
       return self

    def set_number(self, number):
        self._number = number
        return self

    def set_destination(self, destination):
        self._destination = destination
        return self

    def set_price(self, price):
        self._price = price
        return self
    def set_tipus(self, tipus):
        self._tipus = tipus
        return self

    def checking_international_flightnumber(self,_flightnumber):
        i = 0
        j = 0
        for i in range(len(self)):
            # print(_flightnumber, str(_bf[i].get_number()))
            if _flightnumber == str(self.get_number()): return 1
        return 0