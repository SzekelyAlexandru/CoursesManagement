from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, \
    login_required
from app import app, db, lm
from .forms import LoginForm, EditForm, NewSubjectForm, RegisterForm
from .models import Professors, Students, Subjects


@lm.user_loader
def load_user(id):
    if int(id) < 1000:
        return Professors.query.get(int(id))
    elif int(id) >= 1000:
        return Students.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        db.session.add(g.user)
        db.session.commit()


@lm.unauthorized_handler
def unauthorized():
    # do stuff
    return redirect(url_for('login'))


@app.route('/')
@app.route('/index')
@login_required
def index():
    subjects = Subjects.query.filter_by(professor_id=g.user.id).paginate()
    return render_template('index.html',
                           title='Home',
                           user=user,
                           subjects=subjects)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        is_professor = form.is_professor.data
        remember_me = False
        registered_user = None
        if 'remember_me' in form:
            remember_me = True
        if is_professor == True:
            registered_user = Professors.query.filter_by(username=username, password=password).first()
        else:
            registered_user = Students.query.filter_by(username=username, password=password).first()
        if registered_user is None:
            flash('Username or Password is invalid', 'error')
            return redirect(url_for('login'))
        login_user(registered_user, remember=remember_me)
        return redirect(request.args.get('next') or url_for('index'))
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])



@app.route('/register', methods=['GET', 'POST'])
def register():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        name=form.name.data
        surname=form.name.data
        email=form.email.data
        username = form.username.data
        password = form.password.data
        registered_user = Students.query.filter_by(username=username).first()
        if registered_user is not None:
            flash('Username is used!', 'error')
            return redirect(url_for('register'))
        else:
            new_student=Students(name=name, surname=surname, username=username, password=password, email=email, year=1, group=300, profile="none")
            db.session.add(new_student)
            db.session.commit()
            flash("Your account has been created!")
        return redirect(request.args.get('next') or url_for('index'))
    return render_template('register.html',
                           title='Register',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@app.route('/user/<name>_<surname>')
@login_required
def user(name, surname):
    user = Professors.query.filter_by(name=name, surname=surname).first()
    if user is None:
        user = Students.query.filter_by(name=name, surname=surname).first()
    if user is None:
        flash('User %s %s not found.' % name, surname)
        return redirect(url_for('index'))
    return render_template('user.html',
                           user=user)


@app.route('/subject/<subject_id>')
@login_required
def subject(subject_id):
    subject = Subjects.query.filter_by(subject_id=subject_id).first()
    if subject is None:
        flash('User %s not found.' % subject.name)
        return redirect(url_for('index'))
    return render_template('subject.html',
                           user=user,
                           subject=subject)


@app.route('/new_subject', methods=['GET', 'POST'])
@login_required
def newSubject():
    form = NewSubjectForm()
    if form.validate_on_submit():
        prof_id = g.user.id
        subject_name = form.name.data
        year = form.year.data
        semester = form.semester.data
        new_subject = Subjects(professor_id=prof_id, name=subject_name, year=year, semester=semester)
        db.session.add(new_subject)
        db.session.commit()
        flash('Your subject has been created!')
        return redirect(url_for('index'))
    return render_template('newSubject.html',
                           title='New Subject',
                           form=form,
                           user=user)


@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm(g.user.name, g.user.surname)
    if form.validate_on_submit():
        g.user.name = form.name.data
        g.user.surname = form.surname.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit'))
    elif request.method != "POST":
        form.name.data = g.user.name
        form.surname.data = g.user.surname
    return render_template('edit.html', form=form)
