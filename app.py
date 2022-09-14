from flask import Flask ,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.debug = True
db = SQLAlchemy(app)

class Personne(db.Model):
    __tablename__ = 'personne'
    id = db.Column(db.Integer, primary_key=True)
    Ethnicity = db.Column(db.String(80))
    Student = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    Employment = db.Column(db.String(80))
    Country = db.Column(db.String(80))
    Age = db.Column(db.String(80))
    def __init__(self, Ethnicity, Student, Age, gender, Employment, Country):
        self.Ethnicity = Ethnicity
        self.Student = Student
        self.Age = Age
        self.gender = gender
        self.Employment = Employment
        self.Country = Country


@app.route('/personneget', methods=['GET'])
def getpersons():
    all_persons = Personne.query.all()
    result = []
    print(type(all_persons[0]))
    print(all_persons[0])
    for person in all_persons:
        person_data = {}
        person_data['id'] = person.id
        person_data['Ethnicity'] = person.Ethnicity
        person_data['Student'] = person.Student
        person_data['Age'] = person.Age
        person_data['gender'] = person.gender
        person_data['Employment'] = person.Employment
        person_data['Country'] = person.Country

        result.append(person_data)
    return jsonify(result)

@app.route('/personnepost', methods=['POST'])
def addperson():
    data = request.get_json()
    new_person = Personne(data['Ethnicity'], data['Student'], data['age'], data['gender'], data['Employment'], data['Country'])
    db.session.add(new_person)
    db.session.commit()
    return jsonify(data)

# put method
@app.route('/personneput', methods=['PUT'])
def updateperson():
    data = request.get_json()
    person = Personne.query.get(data['id'])
    person.Ethnicity = data['Ethnicity']
    person.Student = data['Student']
    person.Age = data['Age']
    person.gender = data['gender']
    person.Employment = data['Employment']
    person.Country = data['Country']

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