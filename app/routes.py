from flask import render_template, request, flash
from app import app, db,therapists
from app.forms import HouseHoldForm
from app.models import HouseHold, OneTimeGrant,MonthlySupport,HolidayGrant,HeatGrant

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='רשימת לקוחות')


@app.route('/new_household', methods=['GET', 'POST'])
def new_household():

    form = HouseHoldForm()
    if form.validate_on_submit():
        house = HouseHold(
            major_last_name = form.major_last_name.data,
            major_first_name = form.major_first_name.data,
            major_id = form.major_id.data,
            major_phone = form.major_phone.data,
            major_birth_year = form.major_birth_year.data,
            minor_first_name = form.minor_first_name.data,
            minor_last_name = form.minor_last_name.data,
            minor_id = form.minor_id.data,
            minor_phone = form.minor_phone.data,
            address_city = form.address_city.data,
            address_street = form.address_street.data,
            address_house_num = form.address_house_num.data,
            short_description = form.short_description.data,
            current_therapist = form.current_therapist.data
        )
        db.session.add(house)
        db.session.commit()
        flash('Congratulations, you add a new patient!')
        return render_template('index.html', title='רשימת לקוחות')
    return render_template('new_household.html',form=form,list=therapists)


@app.route('/api/data')
def data():
    query = HouseHold.query
    # search filter
    search = request.args.get('search[value]')
    if search:
        query = query.filter(db.or_(
            HouseHold.major_last_name.like(f'%{search}%'),
            HouseHold.major_first_name.like(f'%{search}%'),
            HouseHold.therapist.like(f'%{search}%'),

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
        if col_name not in ['major_first_name', 'major_last_name', 'therapist']:
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
    details = [house.to_dict() for house in query]
    return {
        'data': details,
        'recordsFiltered': total_filtered,
        'recordsTotal': HouseHold.query.count(),
        'draw': request.args.get('draw', type=int),
        }

@app.route('/reports/report_monthly_grant')
def aa():
    return render_template('reports/monthly_support.html', title='רשימת לקוחות')

@app.route('/reports/report_one_grant')
def report_one_grant():
    return render_template('reports/one_time_grant.html', title='רשימת לקוחות')

@app.route('/reports/report_heat_grant')
def report_heat_grant():
    return render_template('reports/heat_grant.html', title='רשימת לקוחות')

@app.route('/reports/report_holiday_grant')
def report_monthly_grant():
    return render_template('reports/holiday_grant.html', title='רשימת לקוחות')


# @app.route('/patient/<user_id>')
# def view_patient(user_id):
#     user = HouseHold.query.get(user_id)
#     interventions = Intervention.query.filter_by(user_id=user_id).order_by(Intervention.date.desc())
#     return render_template('patient.html', user=user,interventions=interventions)

