from flask_wtf import FlaskForm,CSRFProtect
from flask_wtf.file import FileAllowed
from wtforms import StringField,SelectField,IntegerField,SubmitField,DateField, FileField
from wtforms.validators import DataRequired


class StudentInputForm(FlaskForm):
    # id = StringField('Id', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    middle_name = StringField('Middle Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()])
    matric_no = StringField('Matric Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone_number = IntegerField('Phone Number', validators=[DataRequired()])
    college = StringField('College', validators=[DataRequired()])
    department = StringField('Department', validators=[DataRequired()])
    level = IntegerField('Level', validators=[DataRequired()])
    photo = FileField('Photo', validators=[DataRequired(), FileAllowed(['jpg','jpeg','png'])])
    address = StringField('Address', validators=[DataRequired()])
    state_of_origin = StringField('State of Origin', validators=[DataRequired()])
    local_government = StringField('Local Government', validators=[DataRequired()])
    guardian_name = StringField('Guardian Name', validators=[DataRequired()])
    guardian_number = IntegerField('Guardian Number', validators=[DataRequired()])
    guardian_address = StringField('Guardian Address', validators=[DataRequired()])
    submit = SubmitField("Submit")

