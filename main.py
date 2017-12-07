from functions import Select_items
from Connection import Connection
from Order import Order
from Brand import Brand
from User import User
from Product import Product


con = Connection("root", "administr", "computers", "localhost")
print("Таблица продуктов:")
Select_items(con, "product")
print()
print()
con = Connection("root", "administr", "computers", "localhost")
print("Таблица пользователей:")
Select_items(con, "user")
print()
print()

con = Connection("root", "administr", "computers", "localhost")
print("Таблица брендов:")
Select_items(con, "brand")
print()
print()

con = Connection("root", "administr", "computers", "localhost")
print("Таблица заказов:")
Select_items(con, "orders")

