from flask import Flask ,jsonify,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:21060245@localhost/Stage'
app.debug = True
db = SQLAlchemy(app)

class Personne(db.Model):
    __tablename__ = 'personne'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80))
    prenom = db.Column(db.String(80))
    age = db.Column(db.Integer)
    email = db.Column(db.String(120), unique=True)
    def __init__(self, nom, prenom, age, email):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.email = email


@app.route('/personneget', methods=['GET'])
def getpersons():
    all_persons = Personne.query.all()
    result = []
    print(type(all_persons[0]))
    print(all_persons[0])
    for person in all_persons:
        person_data = {}
        person_data['id'] = person.id
        person_data['nom'] = person.nom
        person_data['prenom'] = person.prenom
        person_data['age'] = person.age
        person_data['email'] = person.email
        result.append(person_data)
    return jsonify(result)

@app.route('/personnepost', methods=['POST'])
def addperson():
    data = request.get_json()
    new_person = Personne(data['nom'], data['prenom'], data['age'], data['email'])
    db.session.add(new_person)
    db.session.commit()
    return jsonify(data)

# put method
@app.route('/personneput', methods=['PUT'])
def updateperson():
    data = request.get_json()
    person = Personne.query.get(data['id'])
    person.nom = data['nom']
    person.prenom = data['prenom']
    person.age = data['age']
    person.email = data['email']
    db.session.commit()
    return jsonify(data)
# delete method
@app.route('/personnedelete', methods=['DELETE'])
def deleteperson():
    data = request.get_json()
    person = Personne.query.get(data['id'])
    db.session.delete(person)
    db.session.commit()
    return jsonify(data)
#export to excel

    