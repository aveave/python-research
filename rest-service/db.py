import mysql.connector;

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user= "root",
    password = "secret",
    database = "test"
)

cursor = mydb.cursor()

def create_note_in_db(val):
    sql = "INSERT INTO notes (name, description) VALUES (%s, %s)"
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record inserted")

def get_notes_from_db():
    sql = "SELECT * FROM notes"
    cursor.execute(sql)
    result = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    data = [dict(zip(column_names, row)) for row in result]
    return data

def get_note_by_id_from_db(id):
    sql = "SELECT * FROM notes n WHERE n.id = %s"
    cursor.execute(sql, tuple(id))
    result = cursor.fetchall()
    print('result is ', result)
    column_names = [desc[0] for desc in cursor.description]
    data = [dict(zip(column_names, row)) for row in result]
    return data

