def Select(table, connection):
    c = connection.cursor()
    a = c.execute("SELECT * FROM brand;")
    ready = a.fetchall()
    for i in range(a):
        print(i)
