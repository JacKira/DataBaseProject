from flask import Flask, render_template, request
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'cursovik'
app.config['MYSQL_PORT'] = 3306
app.config['SECRET_KEY'] = '0ur_$uper^puper_$ecret_key!'


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


@app.route('/')
def GetProjsByEmplId(id):
    cur = mysql.connection.cursor()
    query = "CALL GetProjsByEmplId({0})".format(id)
    len = cur.execute(query)
    if(len > 0):
        projs = cur.fetchall()
    else:
        projs = []
    cur.close()
    return projs


@app.route('/')
def GetTransfersByEmplId(id):
    cur = mysql.connection.cursor()
    query = "CALL GetTransfersByEmplId({0})".format(id)
    len = cur.execute(query)
    if(len > 0):
        trans = cur.fetchall()
    else:
        trans = []
    cur.close()
    return trans


@app.route('/')
def GetPrivInfById(id):
    cur = mysql.connection.cursor()
    query = "CALL GetPrivInfById({0})".format(id)
    cur.execute(query)
    inf = cur.fetchone()
    cur.close()
    return inf


@app.route('/')
def GetDeptName(id):
    cur = mysql.connection.cursor()
    query = "SELECT name FROM department dep WHERE dep.ID = {0} ".format(id)
    cur.execute(query)
    name = cur.fetchone()
    cur.close()
    _name = []
    _name.append(name)
    _name.append(id)
    return _name


@app.route('/')
def GetStaffByDepId(id):
    cur = mysql.connection.cursor()
    query = "CALL GetStaffByDepId({0})".format(id)
    len = cur.execute(query)
    if(len > 0):
        staff = cur.fetchall()
    else:
        staff = []
    cur.close()
    return staff


@app.route('/')
def GetReports(id):
    cur = mysql.connection.cursor()
    query = "SELECT * FROM business_trips_report rep WHERE rep.ID = {0}".format(
        id)
    len = cur.execute(query)
    if(len > 0):
        reps = cur.fetchall()
    else:
        reps = []
    cur.close()
    return reps


@app.route('/')
def GetPassport(id):
    cur = mysql.connection.cursor()
    query = "SELECT * FROM passport WHERE Employee = {0}".format(id)
    cur.execute(query)
    pas = cur.fetchone()
    cur.close()
    return pas


@app.route('/Employees/<int:ID_code>')
def GetEmplInfo(ID_code):
    empl = GetEmployee(ID_code)
    trips = GetTripsByEmplId(ID_code)
    inf = GetPrivInfById(ID_code)
    projs = GetProjsByEmplId(ID_code)
    trans = GetTransfersByEmplId(ID_code)
    pas = GetPassport(ID_code)
    return render_template('Employees/employee.html', Employee=empl, Trips=trips, Information=inf, Projects=projs, Transfers=trans, Passport=pas)


@app.route('/Deps/<int:id>')
def GetDeptInf(id):
    name = GetDeptName(id)
    staff = GetStaffByDepId(id)
    return render_template('Deps/Dept.html', Department=name, Staffs=staff)


@app.route('/BusinessTrips/<int:id>')
def GetTripRep(id):
    reps = GetReports(id)
    return render_template('BusinessTrips/Trip.html', Reps=reps)


@app.route('/Employees')
def EmplList():
    empls = GetEmployees()
    return render_template('Employees/list.html', Employees=empls)


@app.route('/Projects')
def ProjsList():
    projs = GetProjs()
    return render_template('Projects/list.html', Projects=projs)


@app.route('/')
def GetProjs():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM projects")
    projs = cur.fetchall()
    cur.close()
    return projs


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
    return render_template('Deps/list.html', Deps=deps)


@app.route('/SalaryReport')
def GetAVGSalByDepReport():
    sal = GetAVGSalByDep()
    return render_template('SalaryReport/list.html', Results=sal)


@app.route('/BusinessReport')
def GetAVGBusByDepReport():
    res = GetAVGBusByDep()
    return render_template('SalaryReport/list.html', Results=res)


@app.route('/BusinessTrips')
def GetTripsAndEmplList():
    rows = GetBusinessTripsAndEmpl()
    return render_template('BusinessTrips/list.html', Results=rows)


@app.route('/Employees/create', methods=('GET', 'POST'))
def AddEmployee():
    """Функция-представление для создания поста"""
    if request.method == 'POST':
        f_name = request.form['First_Name']
        s_name = request.form['Last_Name']
        otch = request.form['Otchestvo']
        staff = request.form['Staffing_Table']
        brd = request.form['BirthDay']
        prem = request.form['Premium']

        if not s_name:
            flash('Вы не добавили фамилию!')
        if not f_name:
            flash('Вы не добавили имя!')
        if not otch:
            flash('Вы не добавили отчество!')
        if not staff:
            flash('Вы не добавили штатное расписание!')
        if not brd:
            flash('Вы не добавили дату рождения!')
        else:
            cur = mysql.connection.cursor()
            query = "INSERT INTO Employee (Last_Name, First_Name, Otchestvo, Staffing_Table, BirthDay, Premium) \n \
             VALUES ('{0}', '{1}', '{2}', {3}, '{4}', {5})".format(s_name, f_name, otch, staff, brd, prem)
            cur.execute(query)
            mysql.connection.commit()
            cur.close()
            flash('ok!')
            return redirect(url_for('EmplList'))
    return render_template('Employees/create.html')


@app.route('/Employees/EditPrivInf<int:id>', methods=('GET', 'POST'))
def EditPrivInf(id):
    """Функция-представление для создания поста"""
    if request.method == 'POST':
        stat = request.form['Status']
        count = request.form['Count']
        adr = request.form['Adres']
        cur = mysql.connection.cursor()
        query = "call UPDPrivInfById({0}, '{1}', {2}, '{3}')".format(id, stat, count, adr)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        flash('ok!')
        return redirect(url_for('GetEmplInfo', ID_code = id))
    inf = GetPrivInfById(id)
    return render_template('Employees/EditPrivInf.html', Inform = inf)     

@app.route('/Employees/AddPassport<int:id>', methods=('GET', 'POST'))
def AddPassport(id):
    """Функция-представление для создания поста"""
    if request.method == 'POST':
        num = request.form['Number']
        date = request.form['Date']
        inst = request.form['Inst']
        if not num:
            flash('Вы не добавили код и номер паспорта!')
        if not date:
            flash('Вы не добавили дату выдачи!')
        if not inst:
            flash('Вы не добавили кем выдано!')
        cur = mysql.connection.cursor()
        query = "INSERT INTO passport (Number, Issue_Date, Institution, Employee) VALUES('{1}', '{2}', '{3}', {0})".format(id, num, date, inst)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        flash('ok!')
        return redirect(url_for('GetEmplInfo', ID_code = id))
    return render_template('Employees/AddPassport.html')      


@app.route('/Employees/<int:id>/delete')
def DeleteEmployee(id):
    """Функция-представление для удаления задачи"""
    cur = mysql.connection.cursor()
    query = "DELETE FROM Employee WHERE ID_code = {0}".format(id)
    cur.execute(query)
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('EmplList'))


app.run(debug=True)
