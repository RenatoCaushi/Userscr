from flask_app.config.mysqlconnection import connectToMySQL


class User:
    db_name='users_cr'
    def __init__(self,data):
        self.id = data['id']
        self.firstname = data['firstname']
        self.lastname = data['lastname']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM users;"""
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for user in results:
            users.append(user)
        return users

    @classmethod
    def Create_user(cls,data):
        query = """INSERT INTO users (first_name, last_name, email) VALUES (%(firstname)s, %(lastname)s, %(email)s)"""
        results = connectToMySQL(cls.db_name).query_db(query,data)
    