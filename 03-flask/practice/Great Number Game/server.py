from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'target_number' not in session:
        session['target_number'] = random.randint(1, 100)
        session['attempts'] = 0
        session['message'] = ""
    
    if request.method == 'POST':
        session['attempts'] += 1
        guess = int(request.form['guess'])
        target_number = session['target_number']
        
        if guess == target_number:
            session.pop('target_number')
            session.pop('attempts')
            return redirect(url_for('success', attempts=session['attempts']))
        elif guess < target_number:
            session['message'] = "Too low! Try again."
        else:
            session['message'] = "Too high! Try again."
    
    return render_template('index.html', message=session['message'])

@app.route('/success/<int:attempts>')
def success(attempts):
    return render_template('success.html', attempts=attempts)

if __name__ == '__main__':
    app.run(debug=True)
