from pprint import pprint
import datetime
from random import randint
import random
from faker import Faker
from datetime import datetime, timedelta
from app import app, db
from app import intervention_types,intervention_status,therapists
from app.models import HouseHold,Intervention
import string

fake = Faker('he_IL')

num = 100

for _ in range(num):

    h = HouseHold(
    major_first_name = fake.first_name(),
    major_last_name = fake.last_name(),
    major_id = fake.msisdn(),
    major_phone = fake.phone_number(),
    major_birth_year = randint(1900, 1960),

    minor_first_name = fake.first_name(),
    minor_last_name = fake.last_name(),
    minor_id = fake.msisdn(),
    minor_phone = fake.phone_number(),

    address_city = fake.city_name(),
    address_street = fake.street_name(),
    address_house_num = fake.building_number(),

    short_description = fake.sentence(nb_words=10, variable_nb_words=False),
    current_therapist =  random.choices(therapists,
                                           weights=None, cum_weights=None,
                                           k=1)[0]
    )
    print(h.major_id,h.minor_id)
    db.session.add(h)
    db.session.commit()
#################################################################################################
num_of_interventions = num * 2
houses = HouseHold.query.all()
all_patients_ids = list()
for id in houses:
    all_patients_ids.append(id.id)

sample_date_year = random.choices(range(2000,2020),
                                           weights=None, cum_weights=None,
                                           k=num_of_interventions)

sample_date_month = random.choices(range(1,12),
                                           weights=None, cum_weights=None,
                                           k=num_of_interventions)


sample_date_day = random.choices(range(1,27),
                                           weights=None, cum_weights=None,
                                           k=num_of_interventions)
sample_ids = random.choices(all_patients_ids,
                                           weights=None, cum_weights=None,
                                           k=num_of_interventions)

sample_intervention_types = random.choices(list(intervention_types.values()),
                                           weights=None, cum_weights=None,
                                           k=num_of_interventions)

sample_therapists = random.choices(therapists,
                                           weights=None, cum_weights=None,
                                           k=num_of_interventions)

sample_intervention_status = random.choices(list(intervention_status.values()),
                                           weights=None, cum_weights=None,
                                           k=num_of_interventions)



Faker.seed(0)
for id,type,therapist,status,year,month,day in zip(sample_ids,
                                                   sample_intervention_types,
                                                    sample_therapists,
                                                   sample_intervention_status,
                                                   sample_date_year,
                                                    sample_date_month,
                                                    sample_date_day
                                                   ):


    i = Intervention(
        in_type = type,
        status = status,
        therapist = therapist,
        date = datetime(year,month,day),
        txt = fake.sentence(nb_words=10, variable_nb_words=False),
        user_id = HouseHold.query.filter_by(id=id).first().id
    )
    db.session.add(i)
    db.session.commit()
    house = HouseHold.query.filter_by(id=id).first()
    house.current_therapist = therapist
    house.current_status = status
    house.current_type = type
    house.last_update = i.date
    db.session.commit()
    print(type,status,therapist,HouseHold.query.filter_by(id=id).first().id)
    print(HouseHold.query.filter_by(id=id).first().current_status,
          HouseHold.query.filter_by(id=id).first().current_type,
          HouseHold.query.filter_by(id=id).first().major_id
          )
    print('-' * 20)
