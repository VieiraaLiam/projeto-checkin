from flask import Flask
from models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all() #creat the database tables if they don't exist
    print("Banco de dados inicializado com sucesso!")
