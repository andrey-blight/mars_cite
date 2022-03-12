from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename


class RegisterForm(FlaskForm):
    email = EmailField('Login / email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Repeat password', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    id_astro = StringField("Id астроонавта", validators=[DataRequired()])
    password_astro = PasswordField("Пароль астронавта", validators=[DataRequired()])
    id_cap = StringField("Id капитана", validators=[DataRequired()])
    password_cap = PasswordField("Пароль капитана", validators=[DataRequired()])
    submit = SubmitField("Доступ")


class FileForm(FlaskForm):
    photo = FileField("Добавит картинку", validators=[FileRequired()])
    submit = SubmitField("Отправить")
