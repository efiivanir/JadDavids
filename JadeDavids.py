from app import app, db
from app.models import HouseHold,OneTimeGrant,MonthlySupport,HeatGrant,HolidayGrant

@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'HouseHold': HouseHold,
            'OneTimeGrant':OneTimeGrant,
            'MonthlySupport':MonthlySupport,
            'HeatGrant':HeatGrant,
            'HolidayGrant':HolidayGrant
            }
