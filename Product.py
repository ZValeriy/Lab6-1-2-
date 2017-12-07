from Connection import *

class Product:
    def __init__(self, db_connection, name, description, cost, brand):
        self.db_connection = db_connection.connection
        self.name = name
        self.description = description
        self.cost = cost
        self.brand = brand

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO product(nameproduct, description, cost, namebrand) VALUES( %s, %s, %s, %s);",
                  (self.name, self.description, self.cost, self.brand))
        self.db_connection.commit()
        c.close()

    @staticmethod
    def select():
        c = Product.db_connection.cursor()
        c.execute("SELECT * FROM product")
        a = c.fetchall()
        for i in a:
            print(i)
