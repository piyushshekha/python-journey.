import mysql.connector

# 1. mysql server connection

conn = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "YOUR_MYSQL_PASSWORD",
    database = "college"
)

# 2. call cursor
cursor = conn.cursor()

# 3. sql query 
cursor.execute("SELECT * FROM student")

# 4. print data using loop
rows = cursor.fetchall
print("--- LIVE DATA FROM MYSQL ---")
for row in rows:
    print(row)
    
# 5 . connection close
conn.close