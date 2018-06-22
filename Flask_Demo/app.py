import cursor as cursor
from flask import Flask
import pypyodbc
connection = pypyodbc.connect('Driver={SQL Server};'
'Server=192.168.21.57;'
'Database=employees;'
'uid=bootcamp;pwd=bootcamp')
cursor = connection.cursor()


app = Flask(__name__)

@app.route('/')
def get():
    SQLCommand = ("SELECT EMPNO ""FROM employees""limit 5")
    cursor.execute(SQLCommand)
    results = cursor.fetchall()
    while results:
        print ("YEmpno " +str(results[0]))

def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
