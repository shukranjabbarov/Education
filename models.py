from extensions import db
import datetime

class Registr(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    surname = db.Column(db.String(), nullable=False)
    birth_date = db.Column(db.Integer(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    confirm_password = db.Column(db.String(), nullable=False)
    photo = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return self.title()

    def __init__(self, name, surname, birthdate, password, confirm_password, photo):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.password = password
        self.confirm_password = confirm_password
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        


