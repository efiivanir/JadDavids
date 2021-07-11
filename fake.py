from pprint import pprint
from random import randint
import random
from faker import Faker
from datetime import datetime, timedelta
from app import app, db
from app import intervention_types,intervention_status,therapists
from app.models import HouseHold,Intervention
fake = Faker('he_IL')
Faker.seed(0)

num = 10
for _ in range(num):
    h = HouseHold(
    major_first_name = fake.first_name(),
    major_last_name = fake.last_name(),
    major_id = fake.msisdn(),
    major_phone = fake.phone_number(),
    major_birth_year = randint(1900, 1950),

    minor_first_name = fake.first_name(),
    minor_last_name = fake.last_name(),
    minor_id = fake.msisdn(),
    minor_phone = fake.phone_number(),

    address_city = fake.city_name(),
    address_street = fake.street_name(),
    address_house_num = fake.building_number(),

    short_description = fake.sentence(nb_words=10, variable_nb_words=False),
    )
    db.session.add(h)
db.session.commit()

num_of_interventions = num * 2
houses = HouseHold.query.all()
all_patients_ids = list()
for id in houses:
    all_patients_ids.append(id.id)


sample_ids = random.choices(all_patients_ids,
                                           weights=None, cum_weights=None,
                                           k=num_of_interventions)

sample_intervention_types = random.choices(list(intervention_types.keys()),
                                           weights=None, cum_weights=None,
                                           k=num_of_interventions)

sample_therapists = random.choices(therapists,
                                           weights=None, cum_weights=None,
                                           k=num_of_interventions)

sample_intervention_status = random.choices(list(intervention_status.keys()),
                                           weights=None, cum_weights=None,
                                           k=num_of_interventions)


Faker.seed(0)
for id,type,therapist,status in zip(sample_ids,sample_intervention_types,
                                    sample_therapists,sample_intervention_status):
    print(type,status,therapist,'aaaa',HouseHold.query.filter_by(id=id).first().id)
    i = Intervention(
        in_type = type,
        status = status,
        therapist = therapist,
        #date = datetime.utcnow,
        txt = fake.sentence(nb_words=10, variable_nb_words=False),
        user_id = HouseHold.query.filter_by(id=id).first().id
    )
    db.session.add(i)
db.session.commit()