from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'users_schema'
}

# Route for Read (All) page
@app.route('/')
def read_all_users():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    # Fetch all users from the database
    query = "SELECT * FROM users_schema.users"
    cursor.execute(query)
    users = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('read_all.html', users=users)

# Route for Create page
@app.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert new user into the database
        query = "INSERT INTO users_schema.users (first_name, email) VALUES (%s, %s)"
        cursor.execute(query, (name, email))
        connection.commit()

        cursor.close()
        connection.close()

        return redirect('/')

    return render_template('create.html')


@app.route('/users/<int:user_id>/show')
def read_one(user_id):
    user = user.query.get_or_404(user_id)
    return render_template('read_one.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    user = user.query.get_or_404(user_id)

    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        user.updated_at = datetime.utcnow()  # Update the 'updated_at' field
        db_config.session.commit()
        return redirect(url_for('read_one', user_id=user.id))

    return render_template('edit_user.html', user=user)

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = user.query.get_or_404(user_id)
    db_config.session.delete(user)
    db_config.session.commit()
    return redirect(url_for('read_all'))

@app.route('/users/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        # Handle form data and create a new user in the database
        # (Assuming you have a form to collect the 'username' and 'email' fields)
        user = user(username=request.form['username'], email=request.form['email'])
        db_config.session.add(user)
        db_config.session.commit()
        return redirect(url_for('read_one', user_id=user.id))  # Redirect to Show page

    return render_template('create_user.html')


if __name__ == '__main__':
    app.run(debug=True)
