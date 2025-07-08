from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User
from app.forms import LoginForm, SignupForm
from app import db

auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')

@auth_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(cpf=form.cpf.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('qst.dashboard'))
        flash('CPF ou senha incorretos', 'error')
    return render_template('auth/signin.html', form=form)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(
            name=form.name.data, cpf=form.cpf.data, birth_date=form.birth_date.data,
            state=form.state.data, study_area=form.study_area.data,
            preparatory=form.preparatory.data, email=form.email.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Usuário cadastrado com sucesso!', 'success')
        return redirect(url_for('auth.signin'))
    return render_template('auth/signup.html', form=form)

@auth_bp.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for('auth.signin'))
