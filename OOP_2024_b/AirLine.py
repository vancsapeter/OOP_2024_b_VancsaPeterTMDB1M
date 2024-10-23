


class AirLine:  # Tartalmazza a járatokat és saját attribútumot, mint például a légitársaság neve.


    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
        return self

#class Flight(AirLine):  # Definiálja a járat alapvető attribútumait (járatszám, célállomás, jegyár).
#    def __init__(self, name, number, destination, price):
#        super().__init__(name)
#        self.name = name
#        self.number = number
#        self.destination = destination
#        self.price = price
#
#    def get_number(self):
#        return self.number
#
#    def get_destination(self):
#        return self.destination
#
#    def get_price(self):
#        return self.price


# class DomesticFlight(Flight):  # Belföldi járatokra vonatkozó osztály, amelyek olcsóbbak és rövidebbek
#     type="Domestic"
#     def __init__(self, name, number, destination, price):
#         super().__init__(name, number, destination, price)
#
#         self.name = name
#         self.number = number
#         self.destination = destination
#         self.price = price
#
#     def get_name(self):
#         return self.name
#
#     def get_number(self):
#         return self.number
#
#     def get_destination(self):
#         return self.destination
#
#     def get_price(self):
#         return self.price
#
#     def get_type(self):
#         return self.type
#
#     def set_name(self, name):
#         self.name = name
#         return self
#
#     def set_number(self, number):
#         self.number = number
#         return self
#
#     def set_destination(self, destination):
#         self.destination = destination
#         return self
#
#     def set_price(self, price):
#         self.price = price
#         return self




# class InternationalFlight(Flight):  # Nemzetközi járatokra vonatkozó osztály, magasabb jegyárakkal.
#     def __init__(self, name, number, destination, price, tp="International"):
#         super().__init__(name, number, destination, price)
#
#         self._name=name
#         self._tipus = tp
#         self._number = number
#         self._destination = destination
#         self._price = price
#     def get_name(self):
#         return self._name
#
#     def get_number(self):
#         return self._number
#
#     def get_destination(self):
#         return self._destination
#
#     def get_price(self):
#         return self._price
#     def get_tipus(self):
#         return self._tipus
#
#
#     def set_name(self, name):
#        self._name=name
#        return self
#
#     def set_number(self, number):
#         self._number = number
#         return self
#
#     def set_destination(self, destination):
#         self._destination = destination
#         return self
#
#     def set_price(self, price):
#         self._price = price
#         return self
#     def set_tipus(self, tipus):
#         self._tipus = tipus
#         return self
#
#     def checking_international_flightnumber(self,_flightnumber):
#         i = 0
#         j = 0
#         for i in range(len(self)):
#             # print(_flightnumber, str(_bf[i].get_number()))
#             if _flightnumber == str(self.get_number()): return 1
#         return 0



# class InternationalTicket(InternationalFlight):  # A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja.
#     def __init__(self, name, number, destination, price, tp, ticket_number, available):
#         super().__init__(name, number, destination, price, tp)
#         self.available = available
#         self.number = number
#         self.ticket_number = ticket_number
#         self.destination = destination
#         self.price = price
#         self.tp = tp
#
#     def set_price(self, price):
#         self.price = price
#         return self
#
#     def set_ticket_number(self, ticket_number):
#         self.ticket_number = ticket_number
#         return self
#
#     def set_available(self, available):
#         self.available = available
#         return self
#     def set_number(self, number):
#         self.number = number
#         return self
#
#     def set_destination(self, destination):
#         self.destination = destination
#         return self
#     def set_tp(self, tp):
#         self.tp = tp
#         return self
#
#
#     def get_ticket_number(self):
#         return self.ticket_number
#
#     def get_available(self):
#         return self.available
#     def get_price(self):
#         return self.price
#     def get_name(self):
#         return self.name
#     def get_destination(self):
#         return self.destination
#     def get_number(self):
#         return self.number
#     def get_tp(self):
#         return self.tp
#
#     def print_booked_ticket(self):
#         if self.available == 0:
#             print(self.name,
#                   self.number,
#                   self.destination,
#                   self.price,
#                   self.tp,
#                   self.ticket_number,
#                   self.available)
#     def checking_ticketid(self, ticketid):
#         if ticketid == self.ticket_number:
#             return True


# class NemzetkoziJegyfoglalas(NemzetkoziJegyek):
#     def __init__(self, name, number, destination, price, , tp, ticket_number, available):
#         super().__init__(name, number, destination, price, tp, ticket_number, available)

# class DomesticTicket(DomesticFlight):  # A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja.
#     def __init__(self, name, number, destination, price,tp, ticket_number, available):
#         super().__init__(name, number, destination, price)
#         self.available = available
#         self.number = number
#         self.ticket_number = ticket_number
#         self.destination = destination
#         self.price = price
#         self.tp = tp
#
#     def set_price(self, price):
#         self.price = price
#         return self
#
#     def set_ticket_number(self, ticket_number):
#         self.ticket_number = ticket_number
#         return self
#
#     def set_available(self, available):
#         self.available = available
#         return self
#
#     def set_number(self, number):
#         self.number = number
#         return self
#
#     def set_destination(self, destination):
#         self.destination = destination
#         return self
#
#     def set_tp(self, tp):
#         self.tp = tp
#         return self
#
#     def get_ticket_number(self):
#         return self.ticket_number
#
#     def get_available(self):
#         return self.available
#
#     def get_price(self):
#         return self.price
#
#     def get_name(self):
#         return self.name
#
#     def get_destination(self):
#         return self.destination
#
#     def get_number(self):
#         return self.number
#
#     def get_tp(self):
#         return self.tp
#
#     def print_booked_ticket(self):
#         if self.available == 0:
#             print(self.name, self.number,
#                   self.destination,
#                   self.price,
#                   self.tp,
#                   self.ticket_number,
#                   self.available)
#
#     def checking_ticketid(self, ticketid):
#         if ticketid == str(self.ticket_number):
#             return True