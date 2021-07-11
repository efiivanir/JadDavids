from app import app, db
from app.models import HouseHold,Intervention

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'HouseHold': HouseHold, 'Intervension': Intervention}