import datetime
import sys
from time import sleep
from AirLine import AirLine
from InternationalFlight import InternationalFlight
from DomesticTicket import DomesticTicket
from DomesticFlight import DomesticFlight
from InternationalTicket import InternationalTicket


# Inícializálás # egy légitársaság, 3 járat és 6 foglalás

AirLine1 = AirLine("TMDB1M")
name=AirLine1.get_name()
international_flights=[
            InternationalFlight(
                name,
                234,
                "New York",
                600)
        ]
domestic_flights=  [
        DomesticFlight(
               name,
                123,
                "Budapest",
                213),
        DomesticFlight(
                name,
                250,
                "Pécs",
                125)
        ]
international_tickets=[
            InternationalTicket(
                name,
                international_flights[0].get_number(),
                international_flights[0].get_destination(),
                international_flights[0].get_price(),
                "International",
                100100,
                0),
            InternationalTicket(
                name,
                international_flights[0].get_number(),
                international_flights[0].get_destination(),
                international_flights[0].get_price(),
                "International",
                100101,
                0),
            InternationalTicket(
                name,
                international_flights[0].get_number(),
                international_flights[0].get_destination(),
                international_flights[0].get_price(),
                "International",
                100102,
                1),
            InternationalTicket(
                name,
                international_flights[0].get_number(),
                international_flights[0].get_destination(),
                international_flights[0].get_price(),
                "International",
                100103,
                1),
            InternationalTicket(
                name,
                international_flights[0].get_number(),
                international_flights[0].get_destination(),
                international_flights[0].get_price(),
                "International",
                100104,
                1),
            InternationalTicket(
                name,
                international_flights[0].get_number(),
                international_flights[0].get_destination(),
                international_flights[0].get_price(),
                "International",
                100105,
                1),
            InternationalTicket(
                name,
                international_flights[0].get_number(),
                international_flights[0].get_destination(),
                international_flights[0].get_price(),
                "International",
                100106,
                1),
            InternationalTicket(
                name,
                international_flights[0].get_number(),
                international_flights[0].get_destination(),
                international_flights[0].get_price(),
                "International",
                100107,
                1),
            InternationalTicket(
                name,
                international_flights[0].get_number(),
                international_flights[0].get_destination(),
                international_flights[0].get_price(),
                "International",
                100108,
                1),
            InternationalTicket(
                name,
                international_flights[0].get_number(),
                international_flights[0].get_destination(),
                international_flights[0].get_price(),
                "International",
                100109,
                1),
            InternationalTicket(
                name,
                international_flights[0].get_number(),
                international_flights[0].get_destination(),
                international_flights[0].get_price(),
                "International",
                100110,
                1)
            ]
#Negatív foglalás teszteléséhez:
# for j in range(len(international_tickets)):
#     international_tickets[j].set_available(0)
domestic_tickets= [
            DomesticTicket(
                name,
                domestic_flights[0].get_number(),
                domestic_flights[0].get_destination(),
                domestic_flights[0].get_price(),
                "Domestic",
                100,
                0),
            DomesticTicket(
                name,
                domestic_flights[0].get_number(),
                domestic_flights[0].get_destination(),
                domestic_flights[0].get_price(),
                "Domestic",
                101,
                0),
            DomesticTicket(
                name,
                domestic_flights[0].get_number(),
                domestic_flights[0].get_destination(),
                domestic_flights[0].get_price(),
                "Domestic",
                102,
                1),
            DomesticTicket(
                name,
                domestic_flights[0].get_number(),
                domestic_flights[0].get_destination(),
                domestic_flights[0].get_price(),
                "Domestic",
                103,
                1),
            DomesticTicket(
                name,
                domestic_flights[0].get_number(),
                domestic_flights[0].get_destination(),
                domestic_flights[0].get_price(),
                "Domestic",
                104,
                1),
            DomesticTicket(
                name,
                domestic_flights[1].get_number(),
                domestic_flights[1].get_destination(),
                domestic_flights[1].get_price(),
                "Domestic",
                112,
                0),
            DomesticTicket(
                name,
                domestic_flights[1].get_number(),
                domestic_flights[1].get_destination(),
                domestic_flights[1].get_price(),
                "Domestic",
                113,
                0),
            DomesticTicket(
                name,
                domestic_flights[1].get_number(),
                domestic_flights[1].get_destination(),
                domestic_flights[1].get_price(),
                "Domestic",
                114,
                1),
            DomesticTicket(
                name,
                domestic_flights[1].get_number(),
                domestic_flights[1].get_destination(),
                domestic_flights[1].get_price(),
                "Domestic",
                115,
                1),
            DomesticTicket(
                name,
                domestic_flights[1].get_number(),
                domestic_flights[1].get_destination(),
                domestic_flights[1].get_price(),
                "Domestic",
                116,
                1),
            DomesticTicket(
                name,
                domestic_flights[1].get_number(),
                domestic_flights[1].get_destination(),
                domestic_flights[1].get_price(),
                "Domestic",
                117,
                1),
            DomesticTicket(
                name,
                domestic_flights[1].get_number(),
                domestic_flights[1].get_destination(),
                domestic_flights[1].get_price(),
                "Domestic",
                118,
                1),
            DomesticTicket(
                name,
                domestic_flights[1].get_number(),
                domestic_flights[1].get_destination(),
                domestic_flights[1].get_price(),
                "Domestic",
                119,
                1),
            DomesticTicket(
                name,
                domestic_flights[1].get_number(),
                domestic_flights[1].get_destination(),
                domestic_flights[1].get_price(),
                "Domestic",
                120,
                1)
        ]

def menu():
    print(f"Kérem válasszon az alábbi menüpontokból")

    print(f"1 - Foglalás")
    print(f"2 - Foglalások megtekintése")
    print(f"3 - Foglalás törlése")
    print(f"0 - Kilépés")
    isint=0
    selection = input(f"Választás:")
    while isint!=1:
        try:
            int(selection)
            isint=1
        except ValueError:
            selection = input(f"A megadott érték nem megfelelő!\n"
                              f"Választás:")
            isint=0

    return selection

def date_validation(_date):
    point1 = _date.find(".")
    point2 = _date.find(".", 5)
    x=0
    if len(_date) != 10:
        print("Nem megfelelő a formátum!")
        x = 0
    elif point1 != 4:
        print("Nem megfelelő a formátum!")
        x = 0
    elif point2 != 7:
        print("Nem megfelelő a formátum!")
        x = 0
    elif int(_date[5:7])>12 or int(_date[5:7])<1:
        print("Nem megfelelő a formátum!")
        x = 0
    elif int(_date[5:7])<1:
        print("Nem megfelelő a formátum!")
        x = 0
    elif int(_date[5:7])==2 and int(_date[8:10])>30:
        print("Hibás dátum!")
        x = 0
    elif int(_date[0:4]) % 4==0 and int(_date[5:7]) == 2  and int(_date[8:10])>29:
        print("Hibás dátum!")
        x = 0
    elif int(_date[0:4]) % 4>0 and int(_date[5:7]) == 2  and int(_date[8:10])>28:
        print("Hibás dátum!")
        x = 0
    elif int(_date[5:7]) not in [1,3,5,7,8,10,12] and int(_date[8:10])>30:
        print("Hibás dátum!")
        x = 0
    else:

        try:
            int(_date[0:4])
            int(_date[8:10])

            if int(_date[0:4]) < datetime.datetime.now().year:
                print("Kérem jövőbeni dátumot adjon meg!")
                x = 0
            elif int(_date[0:4]) == datetime.datetime.now().year and int(_date[5:7]) < datetime.datetime.now().month:
                print("Kérlek jövőbeni dátumot adj meg!")
                x = 0
            elif int(_date[5:7]) == datetime.datetime.now().month and int(_date[8:10]) < datetime.datetime.now().day:
                print("Kérlek jövőbeni dátumot adj meg!")
                x = 0
            else:
                x = 1
        except ValueError:
            print("Nem megfelelő formátum!")
            x = 0
    return x

tst=0
while tst != 1:

    select = int(menu())
    match select:
       case 1:  # Foglalás
           # Dátum megadása
            chk = 0
            while chk != 1:
                date = input(f"Kérem adja meg az indulás időpontját! (Elvárt formátum ÉÉÉÉ.HH.NN)\n")
                # dátum ellenőrzés
                if date_validation(date):
                    chk = 1

            # A járatok kiírása
                    chk2 = 0
                    while chk2 != 1:
                        print(f"Belföldi járatok:")

                        for i in range(len(domestic_flights)):
                            print(f"Légitársaság:{domestic_flights[i].get_name()} "
                                  f"Járatszám: {str(domestic_flights[i].get_number())} "
                                  f"Célállomás: {domestic_flights[i].get_destination()} "
                                  f"Ár: {str(domestic_flights[i].get_price())}€")
                        print(f"\nNemzetközi járatok:")

                        for j in range(len(international_flights)):
                            print(f"Légitársaság:{international_flights[j].get_name()} "
                                  f"Járatszám: {str(international_flights[j].get_number())} "
                                  f"Célállomás: {international_flights[j].get_destination()} "
                                  f"Ár: {str(international_flights[j].get_price())}€\n")
                        # A kiírt járatokból választás

                        flightnumber = ""
                        isflightnumber=0
                        isinteger = 0
                        while isflightnumber !=1  and isinteger != 1:
                            flightnumber = input(f"Kérem adja meg a kívánt járat számát: ")
                            try:
                                int(flightnumber)
                                isinteger = 1

                            except ValueError:
                                print(f"Nem szám került megadásra!")
                                isinteger=0
                        i = 0
                        j = 0
                        x = 0
                        y = 1
                        first_ticket_number=0
                        for i in range(len(domestic_flights)):
                            if flightnumber == str(domestic_flights[i].get_number()): x=1
                        for j in range(len(international_flights)):
                            if flightnumber == str(international_flights[j].get_number()): y=1
                        if x == 1:
                            for i in range(len(domestic_tickets)):
                                if domestic_tickets[i].select_first_available_ticket(flightnumber) != -1:
                                   first_ticket_number=domestic_tickets[i].get_ticket_number()
                                   domestic_tickets[i].set_available(0)
                                   print(f"A foglalás sikeres!")
                                   print(f"A foglalás adatai:"
                                          f"Jegysorszám: {domestic_tickets[i].get_ticket_number()} "
                                          f"Uticél: {domestic_tickets[i].get_destination()} "
                                          f"Ár: {domestic_tickets[i].get_price()} €")
                                   chk2 = 1
                                   break
                            if first_ticket_number==0:
                                print(f"Nincs foglalható jegy a megadott járatra!")
                                chk2 = 1
                        elif y==1:
                            for j in range(len(international_tickets)):
                                if international_tickets[j].select_first_available_ticket(flightnumber)!=-1:
                                    first_ticket_number=international_tickets[j].get_ticket_number()
                                    international_tickets[j].set_available(0)
                                    print(f"A foglalás sikeres!")
                                    print(f"A foglalás adatai:"
                                          f" Jegysorszám: {international_tickets[j].get_ticket_number()} "
                                          f" Uticél: {international_tickets[j].get_destination()} "
                                          f" Ár: {international_tickets[j].get_price()} €")
                                    chk2 = 1
                                    break
                            if first_ticket_number==0:
                                print(f"Nincs foglalható jegy a megadott járatra!")
                                chk2 = 1
                        else:
                              print(f"Kérem a megadott listából válasszon!\n")

       case 2:  # Foglalások megtekintése
            count=0
            for i in range(len(domestic_tickets)):
                count=count+domestic_tickets[i].print_booked_ticket()

            for j in range(len(international_tickets)):
                count=count+international_tickets[j].print_booked_ticket()
            if count == 0:
                print(f"Nincs jelenleg kilistázható foglalás!")

       case 3:  # Foglalás törlése

            isinteger=0
            beolvas2 = input(f"Kérem adja meg a jegyének a számát! \n")
            while isinteger!=1:
                try:
                    int(beolvas2)
                    isinteger=1
                except ValueError:
                    beolvas2 = input(f"A megadott érték hibás!\n"
                                     f"Kérem adja meg a jegyének a számát! \n")
                    isinteger=0

            tmp=0
            for i in range(len(domestic_tickets)):
                if domestic_tickets[i].checking_ticketid(beolvas2):
                    domestic_tickets[i].set_available(1)
                    tmp=1
                    print(f"A {domestic_tickets[i].ticket_number} számú jegyfoglalását töröltük!")

            for j in range(len(international_tickets)):

                if international_tickets[j].checking_ticketid(beolvas2):
                    international_tickets[j].set_available(1)
                    tmp = 1
                    print(f"A {international_tickets[j].ticket_number} számú jegyfoglalását töröltük!")

            if tmp != 1:
                print(f"Nincs ilyen számú jegyfoglalás!")


       case 0:
             print(f"Legyen szép napod!\n")
             sleep(3)
             sys.exit()
       case _:
             print(f"Hibás válasz, a program kilép!\n")
             sys.exit()
    sleep(3)


sys.exit()
