from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange
from app import therapists

class HouseHoldForm(FlaskForm):
    major_first_name = StringField('שם משפחה', validators=[DataRequired()])
    major_last_name = StringField('שם פרטי', validators=[DataRequired()])
    major_id = StringField('תעודת זהות')
    major_phone = StringField('טלפון')
    major_birth_year = StringField('שנת לידה', validators=[DataRequired()])
    
    minor_first_name = StringField('שם משפחה')
    minor_last_name = StringField('שם פרטי')
    minor_id = StringField('תעודת זהות')
    minor_phone = StringField('טלפון')

    address_city = StringField('עיר', validators=[DataRequired()])
    address_street = StringField('רחוב', validators=[DataRequired()])
    address_house_num = StringField('מספר בית', validators=[DataRequired()])

    short_description = TextAreaField('תאור קצר',
                                       render_kw={"rows": 5, "cols": 60},
                                       validators=[Length(min=0, max=140)]
                                    )

    current_therapist = SelectField('מטפל נוכחי', choices=therapists)




    submit = SubmitField('שלח')
