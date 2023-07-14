from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


@app.route('/')
def index():
    session['counter'] = session.get('counter', 0) + 1
    return render_template('index.html', counter=session['counter'], visit_counter=session.get('visit_counter', 0))


@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('index'))


@app.route('/increment', methods=['POST'])
def increment():
    increment_value = int(request.form['increment'])
    session['counter'] += increment_value
    return redirect(url_for('index'))


@app.route('/set_visit_counter', methods=['POST'])
def set_visit_counter():
    visit_counter = int(request.form['visit_counter'])
    session['visit_counter'] = visit_counter
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True)
