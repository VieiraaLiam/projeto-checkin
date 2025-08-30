from models import db, Passenger, Flight, CheckIn

def find_passenger_by_cpf(cpf):
    return Passenger.query.filter_by(cpf=cpf).first()

def create_passenger(name, cpf):
    p = Passenger(name, cpf)
    db.session.add(p)
    db.session.commit()
    return p

def create_flight(number, origin, destiny, company):
    f = Flight(number=number, origin=origin, destiny=destiny, company=company)
    db.session.add(f)
    db.session.commit()
    return f

def do_checkin(passenger, flight):
    checkin = CheckIn(passenger=passenger, flight=flight)
    checkin.checked_in = True
    db.session.add(checkin)
    db.session.commit()
    return checkin

def do_checkout(checkin):
    if checkin.checked_in:
        checkin.checked_in = False
        db.session.commit()
        return True
    return False

