from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://your_username:your_password@localhost/dojos_and_ninjas_schema'
db = SQLAlchemy(app)

# Define the Dojo model
class Dojo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())

# Define the Ninja model
class Ninja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())
    dojo_id = db.Column(db.Integer, db.ForeignKey('dojo.id'), nullable=False)
    dojo = db.relationship('Dojo', backref=db.backref('ninjas', lazy=True))

@app.route('/')
def home():
    return redirect(url_for('dojos'))

@app.route('/dojos', methods=['GET', 'POST'])
def dojos():
    if request.method == 'POST':
        dojo_name = request.form['dojo_name']
        new_dojo = Dojo(name=dojo_name)
        db.session.add(new_dojo)
        db.session.commit()
        return redirect(url_for('dojos'))

    dojos = Dojo.query.all()
    return render_template('dojos.html', dojos=dojos)

@app.route('/dojo/<int:dojo_id>')
def dojo_show(dojo_id):
    dojo = Dojo.query.get_or_404(dojo_id)
    return render_template('dojo_show.html', dojo=dojo)

@app.route('/ninjas', methods=['GET', 'POST'])
def ninjas():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = int(request.form['age'])
        dojo_id = int(request.form['dojo_id'])

        new_ninja = Ninja(first_name=first_name, last_name=last_name, age=age, dojo_id=dojo_id)
        db.session.add(new_ninja)
        db.session.commit()
        return redirect(url_for('dojo_show', dojo_id=dojo_id))

    dojos = Dojo.query.all()
    return render_template('ninjas.html', dojos=dojos)
