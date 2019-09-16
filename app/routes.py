from flask import render_template, flash, redirect, url_for, send_file, jsonify, make_response, request
from app import app, db
from flask_login import current_user, login_user, logout_user
from app.forms import LoginForm, WeighInForm
from app.models import User, WeighIn
from app.processing import get_weight_bf_graph, copy_filelike_to_file
from werkzeug.utils import secure_filename

import os, time

@app.route('/')
@app.route('/index')
def index():
    sandbox = Sand.query.all()
    return render_template('index.html',sandbox=sandbox)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))