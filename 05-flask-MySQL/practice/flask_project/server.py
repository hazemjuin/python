from flask import Flask, render_template, request, redirect
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

if __name__ == '__main__':
    app.run(debug=True)
