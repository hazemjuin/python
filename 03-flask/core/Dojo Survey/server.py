from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        session['gender'] = request.form['gender']
        session['interests'] = request.form.getlist('interests')
        return redirect('/result')
    return render_template('index.html')


@app.route('/result')
def result():
    if 'name' in session:
        name = session['name']
        email = session['email']
        gender = session['gender']
        interests = session['interests']
        session.clear()
        return render_template('result.html', name=name, email=email, gender=gender, interests=interests)
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
