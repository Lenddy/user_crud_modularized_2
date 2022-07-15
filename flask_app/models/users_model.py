from flask_app.config.mysqlconnect import connectToMySQL
from flask_app import db


class User:
    def __init__(self,data):
        self.id = data["id"]
        self.f_name = data["f_name"]
        self.l_name = data["l_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]


    @classmethod
    def get_all(cls):
        query = "select* from users;"
        result = connectToMySQL(db).query_db(query)
        # print(result)
        list_users =[]
        for user in result:
            list_users.append(cls(user))
        print(list_users)
        return list_users


    @classmethod
    def create_user(cls,data):
        query = "insert into users (f_name,l_name,email) values (%(f_name)s,%(l_name)s,%(email)s);"
        result = connectToMySQL(db).query_db(query,data)
        print(result)
        return result


    @classmethod
    def show_one(cls,data):
        query = "select * from users where id = %(id)s"
        result = connectToMySQL(db).query_db(query,data)
        return cls(result[0])


    @classmethod
    def update_one(cls,data):
        query = "update users set f_name= %(f_name)s,l_name = %(l_name)s,email = %(email)s where id = %(id)s;"
        result = connectToMySQL(db).query_db(query,data)
        return result


    @classmethod
    def delete_one(cls,data):
        query = "delete from users where id = %(id)s;"
        result = connectToMySQL(db).query_db(query,data)
        return result