from DomesticFlight import DomesticFlight

class DomesticTicket(DomesticFlight):  # A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja.
    def __init__(self, name, number, destination, price,tp, ticket_number, available):
        super().__init__(name, number, destination, price)
        self._available = available
        self._number = number
        self._ticket_number = ticket_number
        self._destination = destination
        self._price = price
        self._tp = tp

    def __str__(self):
        return (f"Légitársaság: {self._name}, "
                f"Járatszám {self._number}, "
                f"Úticél: {self._destination}, "
                f"Ár: {self._price}€, "
                f"Típus: {self._tp}, "
                f"Jegysorszám: {self._ticket_number}, "
                f"Foglaltság: {self._available}")

    # def set_price(self, price):
    #     self._price = price
    #     return self
    #
    def set_ticket_number(self, ticket_number):
        self._ticket_number = ticket_number
        return self

    def set_available(self, available):
        self._available = available
        return self

    # def set_number(self, number):
    #     self._number = number
    #     return self
    #
    # def set_destination(self, destination):
    #     self._destination = destination
    #     return self

    def set_tp(self, tp):
        self._tp = tp
        return self

    def get_ticket_number(self):
        return self._ticket_number

    def get_available(self):
        return self._available

    # def get_price(self):
    #     return self._price
    #
    # def get_name(self):
    #     return self._name
    #
    # def get_destination(self):
    #     return self._destination
    #
    # def get_number(self):
    #     return self._number

    def get_tp(self):
        return self._tp



    def checking_ticketid(self, ticketid):
        if ticketid == str(self._ticket_number) and self._available == 0:
            return True

    def select_first_available_ticket(self, flightnumber):
        if self._available == 1 and self._number == int(flightnumber):
                return self._ticket_number
        else: return -1

