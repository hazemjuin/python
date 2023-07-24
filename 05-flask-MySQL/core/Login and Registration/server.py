from flask import Flask, render_template, request, redirect, session
from passlib.hash import sha256_crypt
import MySQLdb

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Inside app.py, after the previous code snippet

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle registration or login form submissions
        pass
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')
# Inside app.py, after the previous code snippet

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'register' in request.form:
            username = request.form['username']
            password = request.form['password']

            # Perform additional password validation (at least 1 number and 1 uppercase letter)
            if not any(char.isdigit() for char in password) or not any(char.isupper() for char in password):
                error_msg = "Password must contain at least 1 number and 1 uppercase letter."
                return render_template('index.html', registration_error=error_msg)

            # Hash the password
            hashed_password = sha256_crypt.encrypt(password)

            # Save the user in the database
            try:
                query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                execute_query(query, (username, hashed_password))
                session['username'] = username
                return redirect('/success')
            except Exception as e:
                error_msg = "An error occurred during registration."
                return render_template('index.html', registration_error=error_msg)

    return render_template('index.html')
# Inside app.py, after the previous code snippet

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'register' in request.form:
            # ... (code for user registration)

        elif 'login' in request.form:
            username = request.form['username']
            password = request.form['password']

            # Retrieve the user from the database
            query = "SELECT username, password FROM users WHERE username = %s"
            result = execute_query(query, (username,))
            user = result.fetchone()

            if user and sha256_crypt.verify(password, user[1]):
                # Login successful, store the user in session
                session['username'] = user[0]
                return redirect('/success')
            else:
                # Invalid login
                error_msg = "Invalid login credentials."
                return render_template('index.html', login_error=error_msg)

    return render_template('index.html')
# Inside app.py, after the previous code snippet

@app.route('/success')
def success():
    if 'username' in session:
        return render_template('success.html', username=session['username'])
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

