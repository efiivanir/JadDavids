from flask import render_template, request
from app import app, db
from app.forms import HouseHoldForm
from app.models import HouseHold

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='רשימת לקוחות')


@app.route('/new_household')
def new_household():
    form = HouseHoldForm()
    return render_template('new_household.html',form=form)


@app.route('/api/data')
def data():
    query = HouseHold.query
    # search filter
    search = request.args.get('search[value]')
    if search:
        query = query.filter(db.or_(
            HouseHold.major_last_name.like(f'%{search}%'),
            HouseHold.major_first_name.like(f'%{search}%')
        ))
    total_filtered = query.count()

    # sorting
    order = []
    i = 0
    while True:
        col_index = request.args.get(f'order[{i}][column]')
        if col_index is None:
            break
        col_name = request.args.get(f'columns[{col_index}][data]')
        if col_name not in ['major_first_name', 'major_last_name', 'major_phone']:
            col_name = 'major_first_name'
        descending = request.args.get(f'order[{i}][dir]') == 'desc'
        col = getattr(HouseHold, col_name)
        if descending:
            col = col.desc()
        order.append(col)
        i += 1
    if order:
        query = query.order_by(*order)

        # pagination
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    query = query.offset(start).limit(length)

    # response
    return {
        'data': [house.to_dict() for house in query],
        'recordsFiltered': total_filtered,
        'recordsTotal': HouseHold.query.count(),
        'draw': request.args.get('draw', type=int),
        }
