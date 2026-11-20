import mysql.connector as mysqlc
"""
try:
    mydb = mysqlc.connect(
        host="127.0.0.1",
        user="root",
        password="@Lesego148"
    )

    if mydb.is_connected():
        print("Successfully connected to MySQL!")

except mysqlc.Error as err:
    print(f"Connection failed: {err}")

finally:
    if "mydb" in locals() and mydb.is_connected():
        mydb.close()
"""
