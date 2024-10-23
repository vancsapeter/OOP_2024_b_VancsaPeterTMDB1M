from InternationalFlight import InternationalFlight


class InternationalTicket(InternationalFlight):  # A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja.
    def __init__(self, name, number, destination, price, tp, ticket_number, available):
        super().__init__(name, number, destination, price, tp)
        self.available = available
        self.number = number
        self.ticket_number = ticket_number
        self.destination = destination
        self.price = price
        self.tp = tp

    def set_price(self, price):
        self.price = price
        return self

    def set_ticket_number(self, ticket_number):
        self.ticket_number = ticket_number
        return self

    def set_available(self, available):
        self.available = available
        return self
    def set_number(self, number):
        self.number = number
        return self

    def set_destination(self, destination):
        self.destination = destination
        return self
    def set_tp(self, tp):
        self.tp = tp
        return self


    def get_ticket_number(self):
        return self.ticket_number

    def get_available(self):
        return self.available
    def get_price(self):
        return self.price
    def get_name(self):
        return self.name
    def get_destination(self):
        return self.destination
    def get_number(self):
        return self.number
    def get_tp(self):
        return self.tp

    def print_booked_ticket(self):
        count=0
        if self.available == 0:
            count=count+1
            print(self.name,
                  self.number,
                  self.destination,
                  self.price,
                  self.tp,
                  self.ticket_number,
                  self.available)
        return count
    def checking_ticketid(self, ticketid):
        if ticketid == str(self.ticket_number) and self.available == 0:
            return True

    def select_first_available_ticket(self, flightnumber):
        if self.available == 1 and self.number == int(flightnumber):
            return self.ticket_number
        else: return -1