import MySQLdb


class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.db = db
        self.password = password
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.db
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


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


con = Connection("root", "administr", "computers", "localhost")

with con:
    comp = Product(con, "Lenovo X1", "Small smartbook", 60000, 2)
    comp.save()

