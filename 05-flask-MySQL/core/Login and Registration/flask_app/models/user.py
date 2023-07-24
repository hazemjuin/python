# models/user.py

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        values = (self.username, self.password)
        cursor = db.get_db().cursor()
        cursor.execute(query, values)
        db.get_db().commit()
        cursor.close()
