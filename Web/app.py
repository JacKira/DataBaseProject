from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'cursovik'
app.config['MYSQL_PORT'] = 3306




mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')    
def GetEmployees():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM Employee''')
    out_rows = cur.fetchall()
    cur.close()
    return out_rows


@app.route('/')
def GetEmployee(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Employee WHERE ID_code = ?", (id,))
    empl = cur.fetchone()
    cur.close()
    return empl


@app.route('/Employees')
def EmplList():
    empls = GetEmployees()
    return render_template('Employees/list.html', Employees = empls)

@app.route('/')
def GetDeps():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Department")
    deps = cur.fetchall()
    cur.close()
    return deps

@app.route('/Deps')
def DepsList():
    deps = GetDeps()
    return render_template('Deps/list.html', Deps = deps)


app.run(debug=True)

