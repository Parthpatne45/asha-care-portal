from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'ashacare-secret-key-2026'

# Demo users (ASHA / Anganwadi workers)
USERS = {
    'asha001': {
        'password': '123456',
        'name': 'Sunita Devi',
        'role': 'ASHA Worker',
        'area': 'Ward No. 5, Rural Block'
    },
    'anganwadi01': {
        'password': '123456',
        'name': 'Kamla Bai',
        'role': 'Anganwadi Worker',
        'area': 'Anganwadi Centre - 12'
    }
}

# Sample data for dashboard
BENEFICIARIES = [
    {'id': 1, 'name': 'Priya Sharma', 'type': 'Pregnant', 'month': '6th Month', 'status': 'Active'},
    {'id': 2, 'name': 'Aarav Kumar', 'type': 'Child', 'age': '18 months', 'status': 'Immunization Due'},
    {'id': 3, 'name': 'Meena Patel', 'type': 'Mother', 'child': '2 years', 'status': 'Nutrition Check'},
    {'id': 4, 'name': 'Ramesh Yadav', 'type': 'NCD Screening', 'age': '45 years', 'status': 'Pending'},
]

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('Please login to continue.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Thank you {name}! Your message has been received.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        user = USERS.get(username)
        if user and user['password'] == password:
            session['user'] = {
                'username': username,
                'name': user['name'],
                'role': user['role'],
                'area': user['area']
            }
            flash(f'Welcome, {user["name"]}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'danger')

    return render_template('login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    user = session.get('user')
    return render_template('dashboard.html', user=user, beneficiaries=BENEFICIARIES)


@app.route('/add-beneficiary', methods=['GET', 'POST'])
@login_required
def add_beneficiary():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Beneficiary "{name}" added successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('add_beneficiary.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
