from app import db
from datetime import datetime


class HouseHold(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    major_first_name = db.Column(db.String(32))
    major_last_name = db.Column(db.String(32))
    major_id = db.Column(db.String(9), default='None')
    major_phone = db.Column(db.String(12),default='None')
    major_birth_year = db.Column(db.String(4))

    minor_first_name = db.Column(db.String(32),default='None')
    minor_last_name = db.Column(db.String(32),default='None')
    minor_id = db.Column(db.String(9), default='None')
    minor_phone = db.Column(db.String(12), default='None')

    address_city = db.Column(db.String(32))
    address_street = db.Column(db.String(32))
    address_house_num = db.Column(db.String(4))

    short_description = db.Column(db.String(150), default='None')
    current_therapist = db.Column(db.String(20))
    current_status = db.Column(db.String(20),default='לקוח חדש')
    current_type = db.Column(db.String(20),default='לקוח חדש')
    last_update = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    interventions = db.relationship('Intervention', backref='m_id', lazy='dynamic')

    def __repr__(self):
        return '<major_id {}>'.format(self.major_id)

    def to_dict(self):
        return {
            'major_first_name': self.major_first_name,
            'major_last_name': self.major_last_name,
            'major_id': self.major_id,
            'major_birth_year': self.major_birth_year,
            'major_phone': self.major_phone,
            'current_therapist': self.current_therapist,
            'current_status': self.current_status,
            'current_type': self.current_type,
            'last_update': self.last_update.strftime("%a,%d %b %Y")
        }


class Intervention(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('house_hold.id'))
    in_type = db.Column(db.String(20))
    status = db.Column(db.String(20))
    therapist = db.Column(db.String(20))
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    txt = db.Column(db.String(150))

    def __repr__(self):
        return '<Intervension {}>'.format(self.txt)
