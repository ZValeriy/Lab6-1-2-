class Order:
    def __init__(self, db_connection, idcomp, idus):
        self.db_connection = db_connection.connection
        self.idcomp = idcomp
        self.idus = idus

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO order(idcomp, idus) VALUES( %s, %s);",
                  (self.idcomp, self.idus))
        self.db_connection.commit()
        c.close()
