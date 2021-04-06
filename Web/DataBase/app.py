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
    cur.execute("CALL GetEmployees()")
    out_rows = cur.fetchall()
    cur.close()
    return out_rows


@app.route('/')
def GetEmployee(id):
    cur = mysql.connection.cursor()
    query = "CALL GetEmplInfoById({0})".format(id)
    cur.execute(query)
    empl = cur.fetchone()
    cur.close()
    return empl

@app.route('/')
def GetTripsByEmplId(id):
    cur = mysql.connection.cursor()
    query = "CALL GetTripsByEmplId({0})".format(id)
    len = cur.execute(query)
    if(len > 0):
        trips = cur.fetchall()
    else:
        trips = []
    cur.close()
    return trips

@app.route('/Employees/<int:ID_code>')
def GetEmplInfo(ID_code):
    empl = GetEmployee(ID_code)
    trips = GetTripsByEmplId(ID_code)
    return render_template('Employees/employee.html', Employee = empl, Trips = trips)

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


@app.route('/')
def GetAVGSalByDep():
    cur = mysql.connection.cursor()
    cur.execute("call GetAVGSalByDep()")
    sal = cur.fetchall()
    cur.close()
    return sal

@app.route('/')
def GetAVGBusByDep():
    cur = mysql.connection.cursor()
    cur.execute("call GetAVGBusByDep()")
    sal = cur.fetchall()
    cur.close()
    return sal

@app.route('/')
def GetBusinessTripsAndEmpl():
    cur = mysql.connection.cursor()
    cur.execute("call GetTripsAndEmpl()")
    rows = cur.fetchall()
    cur.close()
    return rows

@app.route('/Deps')
def DepsList():
    deps = GetDeps()
    return render_template('Deps/list.html', Deps = deps)

@app.route('/SalaryReport')
def GetAVGSalByDepReport():
    sal = GetAVGSalByDep()
    return render_template('SalaryReport/list.html', Results = sal)

@app.route('/BusinessReport')
def GetAVGBusByDepReport():
    res = GetAVGBusByDep()
    return render_template('SalaryReport/list.html', Results = res)

@app.route('/BusinessTrips')
def GetTripsAndEmplList():
    rows = GetBusinessTripsAndEmpl()
    return render_template('BusinessTrips/list.html', Results = rows)






app.run(debug=True)

