from flask import Flask, render_template, request, jsonify
import controllers as ctrl
from models import db, Passenger, Flight, CheckIn

app = Flask(__name__)
#rote that shows the index page
@app.route("/")
def home():
    return render_template("index.html")

#api rote for creating a passenger
@app.route("/api/passageiros", methods=["POST"])
def create_passenger():
    data = request.json
    name = data.get("name")
    cpf = data.get("cpf")
    passenger = ctrl.create_passenger(data["name"], data["cpf"])
    return jsonify({"mensagem": "Passageiro criado!"}), 201

#api rote for finding a passenger by CPF
@app.route("/api/checkin", methods=["POST"])
def do_checkin_api():
    data = request.json
    cpf = data["cpf"]
    passenger = ctrl.find_passenger_by_cpf(cpf)
    if not passenger:
        return jsonify({"erro": "Passageiro não encontrado"}), 404

    flight = Flight.query.first()
    if not flight:
        return jsonify({"erro": "Nenhum voo disponível."}), 400

    ctrl.do_checkin(passenger, flight)
    return jsonify({"mensagem": f"Check-in realizado para {passenger.name} no voo {flight.number}."}), 200

if __name__ == "__main__":
    app.run(debug=True)
