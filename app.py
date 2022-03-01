import os.path
import os
from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
@app.route('/index/<title>')
def index(title="Начальная страница"):
    return render_template('base.html', title=title)


@app.route("/training/<prof>")
def training(prof: str):
    css_href = url_for('static', filename="/css/center.css")
    header, img = "Научные симуляторы", url_for('static', filename='images/spaceship_science.jpg')
    if "инженер" in prof.lower() or "строитель" in prof.lower():
        header, img = "Инженерные тренажеры", url_for('static', filename='images/spaceship_engineer.jpg')
    return render_template('training.html', header=header, img_href=img, css_href=css_href)


@app.route("/list_prof/<list_style>")
def list_prof(list_style):
    css_href = url_for('static', filename="/css/center.css")
    profs = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач", "инжинер по терраформированию",
             "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог", "инженер жизнеобеспечения",
             "метеороог", "оператор марсохода", "киберинженер", "штурман", "пилот дронов"]
    return render_template("list.html", css_href=css_href, type=list_style, profs=profs)


@app.route("/answer")
@app.route("/auto_answer")
def questionnaire():
    content = {
        'surname': "Watny",
        'name': "Mark",
        'education': "выше среднего",
        'profession': "штурман марсохода",
        'sex': "male",
        'motivation': "Всегда мечтал застрять на Марсе!",
        'ready': True
    }
    return render_template("auto_answer.html", **content)


class LoginForm(FlaskForm):
    id_astro = StringField("Id астроонавта", validators=[DataRequired()])
    password_astro = PasswordField("Пароль астронавта", validators=[DataRequired()])
    id_cap = StringField("Id капитана", validators=[DataRequired()])
    password_cap = PasswordField("Пароль капитана", validators=[DataRequired()])
    submit = SubmitField("Доступ")


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    css_href = url_for('static', filename="/css/left_photo.css")
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', title="Аварийный доступ", form=form, css_href=css_href)


@app.route('/distribution')
def distribution():
    css_href = url_for('static', filename="/css/center.css")
    crew = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    return render_template("distribution.html", css_href=css_href, crew=crew)


@app.route("/table/<sex>/<int:age>")
def table(sex, age):
    if sex not in ["male", "female"] or not (0 <= age <= 100):
        return "ERROR: Неверные параметры"
    if sex == "male":
        color = (0, 50 + (50 - age), 50)
    else:
        color = (240, 50 + (50 - age), 50)
    color = f"hsl({color[0]},{color[1]}%,{color[2]}%)"
    if age < 21:
        photo_url = url_for('static', filename="/images/small_alien.jpg")
    else:
        photo_url = url_for('static', filename="/images/big_alien.jpg")
    return render_template("table.html", color=color, photo_url=photo_url)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
