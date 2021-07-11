from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class HouseHoldForm(FlaskForm):
    major_first_name = StringField('ראשי: שם משפחה', validators=[DataRequired()])
    major_last_name = StringField('ראשי: שם פרטי', validators=[DataRequired()])
    major_id = StringField('ראשי: תעודת זהות', validators=[DataRequired()])
    major_phone = StringField('ראשי: טלפון', validators=[DataRequired()])
    major_birth_year = StringField('ראשי: שנת לידה', validators=[DataRequired()])
    
    minor_first_name = StringField('משני: שם משפחה', validators=[DataRequired()])
    minor_last_name = StringField('משני: שם פרטי', validators=[DataRequired()])
    minor_id = StringField('משני: תעודת זהות', validators=[DataRequired()])
    minor_phone = StringField('משני: טלפון', validators=[DataRequired()])

    address_city = StringField('כתובת: עיר', validators=[DataRequired()])
    address_street = StringField('כתובת: רחוב', validators=[DataRequired()])
    address_house_num = StringField('כתובת: מספר בית', validators=[DataRequired()])

    short_description = StringField('תאור קצר', validators=[Length(min=0, max=140)])

    submit = SubmitField('שלח')