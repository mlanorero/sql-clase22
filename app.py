import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from flask_migrate import Migrate
#from flask_script import Manager

BASEDIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(BASEDIR, "test.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['ENV']='development'
app.config['DEBUG']=True

#manager = Manager(app)
migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def home():
    return jsonify(('Hola Mundo'))

@app.route('/user', methods=["POST"])
def user():
    user = User()
    user.name = request.json.get("name")
    user.password = request.json.get("password")
    user.email = request.json.get("email")
    user.isActive = request.json.get("isActive")

    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize()), 200

if __name__ == "__main__":
    app.run(host='localhost', port=8080)