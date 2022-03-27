from data.db_session import global_init, create_session
from data.users import User
from data.jobs import Jobs
from data.departments import Departments
from data.forms import *
from data import users_resource

from flask import Flask, render_template, redirect, request, make_response, jsonify, abort
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_restful import Api

global_init(r"db/mars_explorer.db")
app = Flask(__name__)
api = Api(app)
api.add_resource(users_resource.UsersListResource, '/api/v2/users')
api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


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
    jobs = [(db_sess.query(User).filter(User.id == job.team_leader).first(), job, job.categories[0].name) for job in
            db_sess.query(Jobs).all()]
    return render_template("index.html", jobs=jobs)


@app.route("/departments")
def departments():
    db_sess = create_session()
    departs = [(db_sess.query(User).filter(User.id == depart.chief).first(), depart) for depart in
               db_sess.query(Departments).all()]
    return render_template("depart.html", departs=departs)


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


@app.route('/jobs', methods=['GET', 'POST'])
@login_required
def add_job():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = create_session()
        job = Jobs(team_leader=current_user.id, job=form.job.data, work_size=form.work_size.data,
                   collaborators=form.collaborators.data,
                   is_finished=form.is_finished.data)
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('add_job.html', title='Добавление работы', form=form)


@app.route('/add_department', methods=['GET', 'POST'])
@login_required
def add_department():
    form = DepartmentForm()
    if form.validate_on_submit():
        db_sess = create_session()
        depart = Departments(chief=current_user.id, title=form.title.data, members=form.members.data,
                             department_email=form.department_email.data, )
        db_sess.add(depart)
        db_sess.commit()
        return redirect('/departments')
    return render_template('add_depart.html', title='Добавление департамента', form=form)


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_jobs(id):
    form = JobsForm()
    if request.method == "GET":
        db_sess = create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id, Jobs.team_leader == current_user.id).first()
        if job:
            form.job.data = job.job
            form.work_size.data = job.work_size
            form.collaborators.data = job.collaborators
            form.is_finished.data = job.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id, Jobs.team_leader.in_([1, current_user.id])).first()
        if job:
            job.job = form.job.data
            job.work_size = form.work_size.data
            job.collaborators = form.collaborators.data
            job.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('add_job.html', title='Редактирование работы', form=form)


@app.route('/depart/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_depart(id):
    form = DepartmentForm()
    if request.method == "GET":
        db_sess = create_session()
        depart = db_sess.query(Departments).filter(Departments.id == id,
                                                   Departments.chief.in_([1, current_user.id])).first()
        if depart:
            form.title.data = depart.title
            form.members.data = depart.members
            form.department_email.data = depart.department_email
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = create_session()
        depart = db_sess.query(Departments).filter(Departments.id == id,
                                                   Departments.chief.in_([1, current_user.id])).first()
        if depart:
            depart.title = form.title.data
            depart.members = form.members.data
            depart.department_email = form.department_email.data
            db_sess.commit()
            return redirect('/departments')
        else:
            abort(404)
    return render_template('add_depart.html', title='Редактирование департамента', form=form)


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == id, Jobs.team_leader.in_([1, current_user.id])).first()
    if job:
        db_sess.delete(job)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/depart_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def depart_delete(id):
    db_sess = create_session()
    depart = db_sess.query(Departments).filter(Departments.id == id,
                                               Departments.chief.in_([1, current_user.id])).first()
    if depart:
        db_sess.delete(depart)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/departments')


if __name__ == '__main__':
    app.run(port=8080, host='localhost')
