class Passenger:
    def __init__(self, name, cpf):
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("CPF inválido! Deve conter 11 dígitos numéricos")
        self.name = name
        self.cpf = cpf
        self.passagens = [] #flights list

    def add_ticket(self, flight):
        self.tickets.append(flight)

class Flight:
    def __init__(self, number, origin, destiny, company):
        self.number = number
        self.origin = origin
        self.destiny = destiny
        self.company = company

class CheckIn:
    def __init__(self, passenger, flight):
        self.passenger = passenger
        self.flight = flight
        self.checked_in = False
