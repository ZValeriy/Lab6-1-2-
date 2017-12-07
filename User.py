class User:
    def __init__(self, db_connection, login, email, passwd):
        self.db_connection = db_connection.connection
        self.login = login
        self.email = email
        self.passwd = passwd

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO user(login, mail, passw) VALUES( %s, %s, %s);",
                  (self.login, self.email, self.passwd))
        self.db_connection.commit()
        c.close()
