from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

intervention_types = {

    'monthly_support': 'תמיכה חודשית',
    'one_time_grant': 'מענק חד פעמי',
    'holiday_grant': 'מענק לחג',
    'heat_grant': 'מענק חימום'
}

intervention_status = {

    'request': 'הוגשה בקשה',
    'request_confirm': 'בקשה אושרה',
    'pay_completed': 'תשלום הועבר',
}


therapists = [
    'דנה',
    'ענבל',
    'חיה',
    'רות',
]

from app import routes, models
