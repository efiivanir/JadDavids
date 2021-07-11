from app import db
from datetime import datetime


class HouseHold(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    major_first_name = db.Column(db.String(64), index=True)
    major_last_name = db.Column(db.String(64), index=True)
    major_id = db.Column(db.String(64), index=True, unique=True)
    major_phone = db.Column(db.String(64), unique=True)
    major_birth_year = db.Column(db.String(64))

    minor_first_name = db.Column(db.String(64))
    minor_last_name = db.Column(db.String(64))
    minor_id = db.Column(db.String(64), index=True, unique=True)
    minor_phone = db.Column(db.String(64), unique=True)

    address_city = db.Column(db.String(64))
    address_street = db.Column(db.String(64))
    address_house_num = db.Column(db.String(64))

    short_description = db.Column(db.String(64))
    interventions = db.relationship('Intervention', backref='m_id', lazy='dynamic')

    def __repr__(self):
        return '<major_id {}>'.format(self.major_id)

    def to_dict(self):
        return {
            'major_first_name': self.major_first_name,
            'major_last_name': self.major_last_name,
            'major_id': self.major_id,
            'major_birth_year': self.major_birth_year,
            'major_phone': self.major_phone
        }


class Intervention(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('house_hold.id'))
    in_type = db.Column(db.String(20))
    status = db.Column(db.String(20))
    therapist = db.Column(db.String(20))
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    txt = db.Column(db.String(64))

    def __repr__(self):
        return '<Intervension {}>'.format(self.txt)
