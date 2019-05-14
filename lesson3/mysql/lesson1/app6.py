# Author: Ali Azhari

# Select with left join


import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="ali",
    passwd="ali",
    database="chat_db"
)

mycursor = mydb.cursor()

sql = "SELECT  agents.name AS agent, chats.dt AS chat FROM agents \
        LEFT JOIN chats ON agents.id = chats.agent_id"


mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Output

# ('John', datetime.datetime(2019, 5, 14, 12, 54, 43))
# ('John', datetime.datetime(2019, 5, 14, 12, 54, 43))
# ('Joe', datetime.datetime(2019, 5, 14, 12, 54, 43))
# ('Susan', None)
# ('Amy', None)
# ('Betty', None)
# (' Peter', None)
# (' Sandy', None)
# (' Ben', None)
# (' Maria', None)
# (' Peter', None)
# (' Sandy', None)


