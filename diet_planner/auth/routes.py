from flask import Blueprint, render_template, request, redirect, url_for, flash
from diet_planner.data_store import user_manager

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if user_manager.verify_user(username, password):
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('auth/login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if user_manager.create_user(username, password):
            # Auto login after register
            user_manager.verify_user(username, password)
            return redirect(url_for('main.index'))
        else:
            flash('Username already exists', 'error')
    return render_template('auth/register.html')

@auth.route('/logout')
def logout():
    user_manager.logout()
    return redirect(url_for('auth.login'))
