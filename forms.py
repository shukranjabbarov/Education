from flask_wtf import FlaskForm
from wtforms import StringField, TextField, IntegerField, SelectField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, Length

class Register(FlaskForm):
    name = StringField(label='Name: ', validators=[DataRequired(), Length(min=3, max=15)], render_kw = {'placeholder': 'Ad...'})
    surname = StringField(label='Soyad: ', validators = [DataRequired(), Length(min=5, max=20)], render_kw = {'placeholder': 'Soyad...' })
    birth_date = IntegerField(label='Tevellud', validators=[DataRequired()], render_kw = {'placeholder': 'Tevellud...'})
    gender = SelectField(label='Cins: ', choices = ['Kishi', 'Qadin'])
    password = StringField(label='Password: ', validators=[DataRequired(), Length(min=6, max=15)], render_kw = {'placeholder': 'Parol...'})
    confirm_password = StringField(label='Password: ', validators=[DataRequired(), Length(min=6, max=15)], render_kw = {'placeholder': 'Parol...'})
    photo = FileField(label='Foto', validators=[DataRequired()])
    additional_info = TextField(label = 'Qisa melumat', render_kw={ 'placeholder':'Elave Melumat...'})

    