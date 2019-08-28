import sqlite3 as sql 

class Database(object):
    """ Create database if not exist """
    def __init__(self): 
        con = sql.connect("database.db")
        cur = con.cursor()
        cur.execute("create table if not exists users (id integer primary key autoincrement, username text not null UNIQUE, email text not null, password text not null)")
        con.close()

    """ Insert new user into the database """
    def insertUser(self, username, email, password):
        con = sql.connect("database.db")
        try:
            cur = con.cursor()
            cur.execute("INSERT INTO users (username, email, password) VALUES (?,?,?)", (username, email, password))
            con.commit()
        except sql.IntegrityError as err:
            con.close()
            return 0
        finally:
            con.close()
        

    """ Get records of all the users in the database """
    def retrieveUsers(self):
        con = sql.connect("database.db")
        cur = con.cursor()
        cur.execute("SELECT username, email, password FROM users")
        users = cur.fetchall()
        con.close()
        return users

    """ Get an active user """
    def activeUsers(self, username, password):
        con = sql.connect("database.db")
        try:
            cur = con.cursor()
            cur.execute("SELECT username, password FROM users WHERE username = '" + username + "' AND password = '" + password + "'")
            users = cur.fetchall()
            return users
        except sql.Error as err:
            con.close()
            return 0
        finally:
            con.close()
        

    """ Is user valid """
    def isUserValid(self, username, password):
        if len(self.activeUsers(username,password)) > 0:
            return True
        return False
