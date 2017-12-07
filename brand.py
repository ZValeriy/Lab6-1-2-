class Brand:
    def __init__(self, db_connection, name):
        self.db_connection = db_connection.connection
        self.name = name

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO brand(namebrand VALUES( %s);",
                  (self.name))
        self.db_connection.commit()
        c.close()
