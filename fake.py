from pprint import pprint
import datetime
from random import randint
import random
from faker import Faker
from datetime import datetime, timedelta, time
from app import app, db
from app import therapists
from app.models import HouseHold, OneTimeGrant, MonthlySupport, HolidayGrant, HeatGrant
import string

fake = Faker('he_IL')

num = 20

for _ in range(num):
    h = HouseHold(
        major_first_name=fake.first_name(),
        major_last_name=fake.last_name(),
        major_id=fake.msisdn(),
        major_phone=fake.phone_number(),
        major_birth_year=randint(1900, 1960),

        minor_first_name=fake.first_name(),
        minor_last_name=fake.last_name(),
        minor_id=fake.msisdn(),
        minor_phone=fake.phone_number(),

        address_city=fake.city_name(),
        address_street=fake.street_name(),
        address_house_num=fake.building_number(),

        short_description=fake.sentence(nb_words=10, variable_nb_words=False),
        current_therapist=random.choices(therapists,
                                         weights=None, cum_weights=None,
                                         k=1)[0]
    )
    print(h.major_id, h.minor_id)
    db.session.add(h)
    db.session.commit()
#################################################################################################
num_of_interventions = num * 2
houses = HouseHold.query.all()
interventions = ['OneTimeGrant', 'MonthlySupport', 'HolidayGrant', 'HeatGrant']
all_patients_ids = list()
for id in houses:
    all_patients_ids.append(id.id)

sample_date_year = random.choices(range(2000, 2020),
                                  weights=None, cum_weights=None,
                                  k=num_of_interventions)

sample_date_month = random.choices(range(1, 12),
                                   weights=None, cum_weights=None,
                                   k=num_of_interventions)

sample_date_day = random.choices(range(1, 27),
                                 weights=None, cum_weights=None,
                                 k=num_of_interventions)
sample_ids = random.choices(all_patients_ids,
                            weights=None, cum_weights=None,
                            k=num_of_interventions)

sample_interventions = random.choices(interventions,
                                      weights=None, cum_weights=None,
                                      k=num_of_interventions)

sample_therapists = random.choices(therapists,
                                   weights=None, cum_weights=None,
                                   k=num_of_interventions)

for id, type, therapist, year, month, day in zip(sample_ids,
                                                 sample_interventions,
                                                 sample_therapists,
                                                 sample_date_year,
                                                 sample_date_month,
                                                 sample_date_day
                                                 ):
    if type == 'OneTimeGrant':
        inters = OneTimeGrant.query.filter_by(user_id=id).order_by(OneTimeGrant.date_update.desc())
        if inters.all() != []:
            status = inters.first().status
            print(status)
            if status == 'אושרה בקשה' or status == 'נדחתה בקשה':
                status = 'הוגשה בקשה'
                date = inters.first().date_update + timedelta(days=730)
                date_decision = date
            else:
                status = random.choice(['אושרה בקשה', 'נדחתה בקשה'])
                date_decision = inters.first().date_update + timedelta(days=30)
                date = date_decision = inters.first().date_update + timedelta(days=31)
        else:
            print('new')
            status = 'הוגשה בקשה'
            date = datetime(year, month, day)
            date_decision = date

        o = OneTimeGrant(
            user_id=id,
            status=status,
            date_decision=date_decision,
            date_update=date,
            therapist=therapist,
            txt=fake.sentence(nb_words=10, variable_nb_words=False)

        )
        db.session.add(o)
        db.session.commit()
    elif type == 'MonthlySupport':
        pass
    elif type == 'HeatGrant':
        inters = HeatGrant.query.filter_by(user_id=id).order_by(HeatGrant.date_update.desc())
        if inters.all() != []:
            status = inters.first().status
            print(status)
            if status == 'אושרה בקשה' or status == 'נדחתה בקשה':
                status = 'הוגשה בקשה'
                date = inters.first().date_update + timedelta(days=730)
                date_decision = date
            else:
                status = random.choice(['אושרה בקשה', 'נדחתה בקשה'])
                date_decision = inters.first().date_update + timedelta(days=30)
                date = date_decision = inters.first().date_update + timedelta(days=31)
        else:
            print('new')
            status = 'הוגשה בקשה'
            date = datetime(year, month, day)
            date_decision = date

        o = HeatGrant(
            user_id=id,
            status=status,
            date_decision=date_decision,
            date_update=date,
            therapist=therapist,
            txt=fake.sentence(nb_words=10, variable_nb_words=False)

        )
        db.session.add(o)
        db.session.commit()
    elif type == 'HolidayGrant':
        inters = HolidayGrant.query.filter_by(user_id=id).order_by(HolidayGrant.date_update.desc())
        if inters.all() != []:
            status = inters.first().status
            print(status)
            if status == 'אושרה בקשה' or status == 'נדחתה בקשה':
                status = 'הוגשה בקשה'
                date = inters.first().date_update + timedelta(days=730)
                date_decision = date
            else:
                status = random.choice(['אושרה בקשה', 'נדחתה בקשה'])
                date_decision = inters.first().date_update + timedelta(days=30)
                date = date_decision = inters.first().date_update + timedelta(days=31)
        else:
            print('new')
            status = 'הוגשה בקשה'
            date = datetime(year, month, day)
            date_decision = date

        o = HolidayGrant(
            user_id=id,
            status=status,
            date_decision=date_decision,
            date_update=date,
            therapist=therapist,
            txt=fake.sentence(nb_words=10, variable_nb_words=False)

        )
        db.session.add(o)
        db.session.commit()
#
#
#     i = Intervention(
#         in_type = type,
#         status = status,
#         therapist = therapist,
#         date = datetime(year,month,day),
#         txt = fake.sentence(nb_words=10, variable_nb_words=False),
#         user_id = HouseHold.query.filter_by(id=id).first().id
#     )
#     db.session.add(i)
#     db.session.commit()
#     house = HouseHold.query.filter_by(id=id).first()
#     house.current_therapist = therapist
#     house.current_status = status
#     house.current_type = type
#     house.last_update = i.date
#     db.session.commit()
#     print(type,status,therapist,HouseHold.query.filter_by(id=id).first().id)
#     print(HouseHold.query.filter_by(id=id).first().current_status,
#           HouseHold.query.filter_by(id=id).first().current_type,
#           HouseHold.query.filter_by(id=id).first().major_id
#           )
#     print('-' * 20)
