from flask_app.config.mysqlconnection import connectToMySQL


class User:
    db_name='usermodularised'
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
        query = """INSERT INTO users (firstname, lastname, email) VALUES (%(firstname)s, %(lastname)s, %(email)s)"""
        results = connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_user_by_id(cls, data):
        query= 'SELECT * FROM users WHERE users.id = %(user_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results[0]

    @classmethod
    def destroyUser(cls, data):
        query= 'DELETE FROM users WHERE users.id = %(user_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def editUser(cls, data):
        query= 'Update users set firstname=%(firstname)s, lastname= %(lastname)s, email=%(email)s, updated_at=NOW() WHERE users.id = %(user_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)