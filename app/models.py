from app import db
from datetime import datetime


class HouseHold(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    major_first_name = db.Column(db.String(32))
    major_last_name = db.Column(db.String(32))
    major_id = db.Column(db.String(9))
    major_phone = db.Column(db.String(12))
    major_birth_year = db.Column(db.String(4))

    minor_first_name = db.Column(db.String(32))
    minor_last_name = db.Column(db.String(32))
    minor_id = db.Column(db.String(9))
    minor_phone = db.Column(db.String(12))

    address_city = db.Column(db.String(32))
    address_street = db.Column(db.String(32))
    address_house_num = db.Column(db.String(4))

    short_description = db.Column(db.String(150))
    therapist = db.Column(db.String(20))

    create_date = db.Column(db.DateTime, index=True,nullable=False)

    # inter_monthly_support_status = db.Column(db.String(20))
    # inter_monthly_support_date_start = db.Column(db.DateTime, index=True)
    # inter_monthly_support_num_of_months = db.Column(db.String(20))
    # inter_monthly_support_date_update = db.Column(db.DateTime, index=True)
    #
    # inter_one_time_grant_status = db.Column(db.String(20))
    # inter_one_time_grant_date_decision = db.Column(db.DateTime, index=True)
    # inter_one_time_grant_date_update = db.Column(db.DateTime, index=True)
    #
    # inter_holiday_grant_status = db.Column(db.String(20))
    # inter_holiday_grant_date_decision = db.Column(db.DateTime, index=True)
    # inter_holiday_grant_date_update = db.Column(db.DateTime, index=True)
    #
    # inter_heat_grant_status = db.Column(db.String(20))
    # inter_heat_grant_date_decision = db.Column(db.DateTime, index=True)
    # inter_heat_grant_date_update = db.Column(db.DateTime, index=True)
    
    inter_monthly_support = db.relationship('MonthlySupport', backref='m_id', lazy='dynamic')
    inter_one_time_grant = db.relationship('OneTimeGrant', backref='m_id', lazy='dynamic')
    inter_holiday_grant = db.relationship('HolidayGrant', backref='m_id', lazy='dynamic')
    inter_heat_grant = db.relationship('HeatGrant', backref='m_id', lazy='dynamic')

    def __repr__(self):
        return '<major_id {}>'.format(self.major_id)

    def to_dict(self):
        return {
            'major_first_name': self.major_first_name,
            'major_last_name': self.major_last_name,
            'major_id': self.major_id,
            'major_birth_year': self.major_birth_year,
            'major_phone': self.major_phone,
            'therapist': self.therapist,
            'create_date': self.create_date.strftime("%a, %-d %b %Y"),


            # 'inter_monthly_support_status': self.inter_monthly_support_status ,
            # 'inter_monthly_support_date_start':
            #     self.inter_monthly_support_date_start.strftime("%b %Y") ,
            # 'inter_monthly_support_num_of_months': self.inter_monthly_support_num_of_months ,
            # 'inter_monthly_support_date_date_update':
            #     self.inter_monthly_support_date_update.strftime("%a, %-d %b %Y"),
            # 'inter_monthly_support_date_decision':
            #     self.inter_monthly_support_date_decision.strftime("%b %Y"),
            #
            #
            # 'inter_one_time_grant_status': self.inter_one_time_grant_status ,
            # 'inter_one_time_grant_date_decision': self.inter_one_time_grant_date_decision.strftime("%b %Y") ,
            # 'inter_one_time_grant_date_update':
            #     self.inter_one_time_grant_date_update.strftime("%a, %-d %b %Y"),
            #
            # 'inter_heat_grant_status': self.inter_heat_grant_status ,
            # 'inter_heat_grant_date_decision': self.inter_heat_grant_date_decision.strftime("%b %Y"),
            # 'inter_heat_grant_date_update':
            #     self.inter_heat_grant_date_update.strftime("%a, %-d %b %Y"),
            #
            # 'inter_holiday_grant_status': self.inter_holiday_grant_status ,
            # 'inter_holiday_grant_date_decision': self.inter_holiday_grant_date_decision.strftime("%b %Y"),
            # 'inter_holiday_grant_date_update':
            #     self.inter_holiday_grant_date_update.strftime("%a, %-d %b %Y"),

        }


class MonthlySupport(db.Model):
    status_types = ['הוגשה בקשה', 'אושרה בקשה', 'נדחתה בקשה']
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('house_hold.id'))
    status = db.Column(db.String(20))
    date_start = db.Column(db.DateTime, index=True)
    num_of_months = db.Column(db.Integer)
    date_update = db.Column(db.DateTime, index=True)
    date_decision = db.Column(db.DateTime, index=True)
    therapist = db.Column(db.String(20))
    txt = db.Column(db.String(150))

    def __repr__(self):
        return '<MonthlySupport {} {} {}>'.format(self.user_id, self.status, self.date_decision)


class OneTimeGrant(db.Model):
    status_types = ['הוגשה בקשה', 'אושרה בקשה', 'נדחתה בקשה']
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('house_hold.id'))
    status = db.Column(db.String(20))
    date_update = db.Column(db.DateTime, index=True)
    date_decision = db.Column(db.DateTime, index=True)
    therapist = db.Column(db.String(20))
    txt = db.Column(db.String(150))

    def __repr__(self):
        return '<OneTimeGrant {} {} {}>'.format(self.user_id, self.status, self.date_decision)


class HolidayGrant(db.Model):
    status_types = ['הוגשה בקשה', 'אושרה בקשה', 'נדחתה בקשה']

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('house_hold.id'))
    status = db.Column(db.String(20))
    date_update = db.Column(db.DateTime, index=True)
    date_decision = db.Column(db.DateTime, index=True)
    therapist = db.Column(db.String(20))
    txt = db.Column(db.String(150))

    def __repr__(self):
        return '<HolydayGrant {} {} {}>'.format(self.user_id, self.status, self.date_decision)


class HeatGrant(db.Model):
    status_types = ['הוגשה בקשה', 'אושרה בקשה', 'נדחתה בקשה']
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('house_hold.id'))
    status = db.Column(db.String(20))
    date_update = db.Column(db.DateTime, index=True)
    date_decision = db.Column(db.DateTime, index=True)
    txt = db.Column(db.String(150))
    
    def __repr__(self):
        return '<HeatGrant {} {} {}>'.format(self.user_id, self.status, self.date_decision)
