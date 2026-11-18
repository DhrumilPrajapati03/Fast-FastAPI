# import json

# shipments = {}

# # print("before load:", shipments)
# with open("shipments.json") as json_file:
#     data = json.load(json_file)

#     for value in data:
#         shipments[value["id"]] = value

# def save():
#     with open("shipments.json", "w") as json_file:
#         json.dump(
#             list(shipments.values()),
#             json_file
#         )

# Sqlite db

import sqlite3

connection = sqlite3.connect("sqlite.db")
cursor = connection.cursor()

# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS shipment(
#                id INTEGER,
#                content TEXT, 
#                weight REAL,
#                status TEXT)""")

# cursor.execute("""
#     INSERT INTO shipment 
#     VALUES (12702, 'palm trees', 19, 'in-transit')
#     """)
# connection.commit()

cursor.execute("""
    SELECT * FROM shipment
""")
result = cursor.fetchall()
print(result)
connection.close()
