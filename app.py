from data.db_session import global_init, create_session
from data.users import User
from data.jobs import Jobs
from data.forms import *

import os.path
import os
import json

from flask import Flask, url_for, render_template, redirect, request, make_response, session
from flask_login import LoginManager, login_manager, login_user, login_required, logout_user

global_init(r"db/mars_explorer.db")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@login_manager.user_loader
def load_user(user_id):
    db_sess = create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def index():
    db_sess = create_session()
    jobs = [(db_sess.query(User).filter(User.id == job.team_leader).first(), job) for job in db_sess.query(Jobs).all()]
    return render_template("index.html", jobs=jobs)


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


@app.route('/gallery', methods=["GET", "POST"])
def gallery():
    form = FileForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        print(filename)
        f.save(os.path.join(r'static/carousel_images', filename))
        return redirect('/gallery')
    images_list = [url_for('static', filename=f"/carousel_images/{el}") for el in os.listdir("static/carousel_images")]
    return render_template("gallery.html", images=images_list, r=range(len(images_list)), form=form)


@app.route("/member")
def member():
    with open('templates/members.json', encoding='utf-8') as file:
        data = json.load(file)
    print(data)
    return render_template("member.html", list=data)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='localhost')
