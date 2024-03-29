from flask import Flask, render_template, request
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'cursovik_v2'
app.config['MYSQL_PORT'] = 3306
app.config['SECRET_KEY'] = '0ur_$uper^puper_$ecret_key!'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL(app)
priv = True

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index.html', methods=('GET', 'POST'))
def Login():
    if request.method == 'POST':
        log = request.form['Login']
        psswrd = request.form['Password']
        if(log == 'root') and (psswrd == 'root') or (log == 'bookkeeper') and (psswrd == '1234'):
            global priv
            priv = True
            if(log == 'bookkeeper'):
                priv = False
            return render_template('home.html', Priviliges = priv)
    return render_template('index.html')


@app.route('/')
def GetProjById(id):
    cur = mysql.connection.cursor()
    query = "SELECT * FROM projects WHERE project_key = {0}".format(id)
    cur.execute(query)
    proj = cur.fetchone()
    cur.close()
    return proj


@app.route('/')
def GetEmployees():
    cur = mysql.connection.cursor()
    cur.execute("CALL GetEmployees()")
    out_rows = cur.fetchall()
    cur.close()
    return out_rows

@app.route('/')
def GetPositions():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Position")
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
def GetEmployeeStaffById(id):
    cur = mysql.connection.cursor()
    query = "CALL GetEmployeeStaffById({0})".format(id)
    cur.execute(query)
    empl = cur.fetchone()
    cur.close()
    return empl

@app.route('/')
def GetEmplInfByProjId(id):
    cur = mysql.connection.cursor()
    query = "CALL GetEmplInfByProjId({0})".format(id)
    if(cur.execute(query) > 0):
        empls = cur.fetchall()
    else:
        empls = []
    cur.close()
    return empls

@app.route('/')
def GetTripById(id):
    cur = mysql.connection.cursor()
    query = "SELECT * FROM business_trips WHERE ID = {0} ".format(id)
    cur.execute(query)
    trip = cur.fetchone()
    cur.close()
    return trip

@app.route('/')
def GetEmpl(id):
    cur = mysql.connection.cursor()
    query = "SELECT * FROM Employee WHERE ID_CODE = {0}".format(id)
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
def GetStaffAndDept():
    cur = mysql.connection.cursor()
    query = "CALL GetStaffAndDept()"
    cur.execute(query)
    staff = cur.fetchall()
    cur.close()
    return staff

@app.route('/')
def GetReports(id):
    cur = mysql.connection.cursor()
    query = "SELECT * FROM business_trips_report rep WHERE rep.Businnes_Trips = {0}".format(
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

@app.route('/')
def GetEmplFromProjById(id):
    cur = mysql.connection.cursor()
    query = "CALL GetEmplFromProjById({0})".format(id)
    cur.execute(query)
    empls = cur.fetchall()
    cur.close()
    return empls



@app.route('/Employees/<int:ID_code>')
def GetEmplInfo(ID_code):
    empl = GetEmployee(ID_code)
    trips = GetTripsByEmplId(ID_code)
    inf = GetPrivInfById(ID_code)
    projs = GetProjsByEmplId(ID_code)
    trans = GetTransfersByEmplId(ID_code)
    pas = GetPassport(ID_code)
    return render_template('Employees/employee.html', Employee=empl, Trips=trips, Information=inf, Projects=projs, Transfers=trans, Passport=pas, Priviliges = priv)


@app.route('/Deps/<int:id>')
def GetDeptInf(id):
    name = GetDeptName(id)
    staff = GetStaffByDepId(id)
    return render_template('Deps/Dept.html', Department=name, Staffs=staff, Priviliges = priv)

@app.route('/Projects/<int:id>')
def GetProjInf(id):
    proj = GetProjById(id)
    empls = GetEmplInfByProjId(id)
    return render_template('Projects/Proj.html', Project = proj, Empls = empls, Priviliges = priv)


@app.route('/BusinessTrips/<int:id>')
def GetTripRep(id):
    reps = GetReports(id)
    return render_template('BusinessTrips/Trip.html', Reps=reps, ID = id, Priviliges = priv)


@app.route('/Employees')
def EmplList():
    empls = GetEmployees()
    return render_template('Employees/list.html', Employees=empls, Priviliges = priv)


@app.route('/Projects')
def ProjsList():
    projs = GetProjs()
    return render_template('Projects/list.html', Projects=projs, Priviliges = priv)


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
    return render_template('Deps/list.html', Deps=deps, Priviliges = priv)


@app.route('/SalaryReport')
def GetAVGSalByDepReport():
    sal = GetAVGSalByDep()
    return render_template('SalaryReport/list.html', Results=sal, Priviliges = priv)


@app.route('/BusinessReport')
def GetAVGBusByDepReport():
    res = GetAVGBusByDep()
    return render_template('BusinessReport/list.html', Results=res, Priviliges = priv)


@app.route('/BusinessTrips')
def GetTripsAndEmplList():
    rows = GetBusinessTripsAndEmpl()
    return render_template('BusinessTrips/list.html', Results=rows, Priviliges = priv)


@app.route('/Employees/create', methods=('GET', 'POST'))
def AddEmployee():
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
    staff = GetStaffAndDept()            
    return render_template('Employees/create.html', Staff = staff, Priviliges = priv)



@app.route('/Employees/EditEmployee<int:ID_code>', methods=('GET', 'POST'))
def EditEmployee(ID_code):
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
            query = "CALL UPDEmployee({0}, '{1}',  '{2}', '{3}', {4}, '{5}', {6})".format(ID_code, s_name, f_name, otch, staff, brd, prem)
            cur.execute(query)
            mysql.connection.commit()
            cur.close()
            flash('ok!')
            return redirect(url_for('GetEmplInfo', ID_code = ID_code))
    inf = GetEmpl(ID_code)
    staff = GetStaffAndDept()
    return render_template('Employees/EditInf.html', Inf = inf,  Staff = staff, Priviliges = priv)

@app.route('/Employees/EditPrivInf<int:id>', methods=('GET', 'POST'))
def EditPrivInf(id):
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
    return render_template('Employees/EditPrivInf.html', Inform = inf, Priviliges = priv)     

@app.route('/Employees/AddPassport<int:id>', methods=('GET', 'POST'))
def AddPassport(id):
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
    return render_template('Employees/AddPassport.html', Priviliges = priv)      

@app.route('/Deps/create', methods=('GET', 'POST'))
def AddDept():
    if request.method == 'POST':
        name = request.form['Name']

        if not name:
            flash('Вы неввели название отдела!')
     
        cur = mysql.connection.cursor()
        query = "INSERT INTO department (Name) VALUES('{0}')".format(name)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        flash('ok!')
        return redirect(url_for('DepsList'))
    return render_template('Deps/create.html', Priviliges = priv) 


@app.route('/Projects/create', methods=('GET', 'POST'))
def AddProj():
    if request.method == 'POST':
        name = request.form['Name']

        if not name:
            flash('Вы неввели название проекта!')
     
        cur = mysql.connection.cursor()
        query = "INSERT INTO projects (project_name) VALUES('{0}')".format(name)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        flash('ok!')
        return redirect(url_for('ProjsList'))
    return render_template('Projects/create.html', Priviliges = priv) 

@app.route('/Projects/<int:id>/edit', methods=('GET', 'POST'))
def EditProj(id):
    if request.method == 'POST':
        name = request.form['Name']

        if not name:
            flash('Вы неввели название проекта!')
     
        cur = mysql.connection.cursor()
        query = "UPDATE projects SET project_name = '{0}' WHERE project_key = {1}".format(name, id)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        flash('ok!')
        return redirect(url_for('ProjsList'))
    proj = GetProjById(id)
    return render_template('Projects/edit.html', Project = proj, Priviliges = priv) 


@app.route('/Employees/<int:id>/delete')
def DeleteEmployee(id):
    cur = mysql.connection.cursor()
    query = "DELETE FROM Employee WHERE ID_code = {0}".format(id)
    cur.execute(query)
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('EmplList'))


@app.route('/Deps/AddStaffTable<int:id>', methods=('GET', 'POST'))
def AddStaffTable(id):
    if request.method == 'POST':
        pos = request.form['Position']
        num = request.form['Number']
        if not num:
            flash('Вы не указали квоту!')
        if not pos:
            flash('Вы не указали должность!')
        cur = mysql.connection.cursor()
        query = "INSERT INTO staffing_table (Position, Count, Dept) VALUES({0}, {1}, {2})".format(pos, num, id)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        flash('ok!')
        return redirect(url_for('GetDeptInf', id = id)) 
    pos = GetPositions()
    return render_template('Deps/AddStaffTable.html', Pos = pos, Priviliges = priv)  


@app.route('/BusinessTrips/create', methods=('GET', 'POST'))
def AddBusinessTrip():
    if request.method == 'POST':
        empl = request.form['Employee']
        city = request.form['City']
        targ = request.form['Target']
        s_date = request.form['StartDate']
        e_date = request.form['EndDate']
        expense = request.form['Expense']

        if not empl:
            flash('Вы не указали работника!')
        if not city:
            flash('Вы не указали город!')
        if not targ:
            flash('Вы не указали цель!')
        if not s_date:
            flash('Вы не указали дату начала!')
        if not e_date:
            flash('Вы не указали дату окончания!')
        if not expense:
            flash('Вы не указали аванс!')
        else:
            cur = mysql.connection.cursor()
            query = "INSERT INTO business_trips (Employee, City, Target, Start_Date, End_Date, Prepaid_Expense) \n \
             VALUES ({0}, '{1}', '{2}', '{3}', '{4}', {5})".format(empl, city, targ, s_date, e_date, expense)
            cur.execute(query)
            mysql.connection.commit()
            cur.close()
            flash('ok!')
            return redirect(url_for('GetTripsAndEmplList'))
    empls = GetEmployees()            
    return render_template('BusinessTrips/create.html', Empls = empls, Priviliges = priv)

@app.route('/BusinessTrips/edit<int:ID>', methods=('GET', 'POST'))
def EditBusinessTrip(ID):
    if request.method == 'POST':
        empl = request.form['Employee']
        city = request.form['City']
        targ = request.form['Target']
        s_date = request.form['StartDate']
        e_date = request.form['EndDate']
        expense = request.form['Expense']

        if not empl:
            flash('Вы не указали работника!')
        if not city:
            flash('Вы не указали город!')
        if not targ:
            flash('Вы не указали цель!')
        if not s_date:
            flash('Вы не указали дату начала!')
        if not e_date:
            flash('Вы не указали дату окончания!')
        if not expense:
            flash('Вы не указали аванс!')
        else:
            cur = mysql.connection.cursor()
            query = "CALL UPDBusinessTrip({0}, '{1}',  '{2}', '{3}', '{4}', '{5}', {6})".format(ID, empl, city, targ, s_date, e_date, expense)
            cur.execute(query)
            mysql.connection.commit()
            cur.close()
            flash('ok!')
            return redirect(url_for('GetTripsAndEmplList'))
    empls = GetEmployees()   
    trip = GetTripById(ID)         
    return render_template('BusinessTrips/edit.html', Trip = trip,  Empls = empls, Priviliges = priv)


@app.route("/Deps/<int:id>", methods= ['POST'])
def DeleteDept(id):
    """Функция-представление для удаления отдела"""
    cur = mysql.connection.cursor()
    query = "DELETE FROM department WHERE ID = {0}".format(id)
    cur.execute(query)
    mysql.connection.commit()
    cur.close()
    flash("Отдел удален!")
    return redirect(url_for('DepsList'))


@app.route("/Projects/<int:id>", methods= ['POST'])
def DeleteProj(id):
    """Функция-представление для удаления отдела"""
    cur = mysql.connection.cursor()
    query = "DELETE FROM projects WHERE project_key = {0}".format(id)
    cur.execute(query)
    mysql.connection.commit()
    cur.close()
    flash("Проект удален!")
    return redirect(url_for('ProjsList'))



@app.route("/BuisinessTrips/<int:id>", methods= ['POST'])
def DeleteBuisinessTrip(id):
    """Функция-представление для удаления отдела"""
    cur = mysql.connection.cursor()
    query = "DELETE FROM business_trips WHERE ID = {0}".format(id)
    cur.execute(query)
    mysql.connection.commit()
    cur.close()
    flash("Командировка удалена!")
    return redirect(url_for('GetTripsAndEmplList'))



@app.route("/Employees/<int:id><int:ID_c>", methods= ['POST'])
def DeleteEmplTransfer(id, ID_c):
    """Функция-представление для удаления отдела"""
    cur = mysql.connection.cursor()
    query = "DELETE FROM employee_transfers WHERE ID = {0}".format(id)
    cur.execute(query)
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('GetEmplInfo', ID_code = ID_c))


@app.route('/BusinessTrips/createReport<int:id>', methods=('GET', 'POST'))
def AddBusinessTrips(id):
    if request.method == 'POST':
        date = request.form['Date']
        purp = request.form['Purpose']
        val = request.form['Value']
        if not date:
            flash('Вы не указали дату!')
        if not purp:
            flash('Вы не указали обоснование!')
        if not val:
            flash('Вы не указали обоснование!')
        cur = mysql.connection.cursor()
        query = "INSERT INTO  business_trips_report (Date, Purpose_Payment, Value, Businnes_Trips) VALUES('{0}', '{1}', {2}, {3})".format(date, purp, val, id)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        flash('ok!')
        return redirect(url_for('GetTripRep', id = id)) 
    return render_template('BusinessTrips/createReport.html', Priviliges = priv)    

@app.route('/Employees/createTransfer<int:ID_code>', methods=('GET', 'POST'))
def createTransfer(ID_code):
    if request.method == 'POST':
        justi = request.form['Justification']
        num = request.form['Order_Number']
        date = request.form['Order_Date']
        staff = request.form['Staffing_Table']

        if not justi:
            flash('Вы не добавили причину перевода')
        if not num:
            flash('Вы не добавили номер приказа')
        if not date:
            flash('Вы не добавили дату приказа!')
        if not staff:
            flash('Вы не добавили штатное расписание!')
        else:
            cur = mysql.connection.cursor()
            query = "CALL InsEmplTrans({0}, {1},  '{2}', '{3}', '{4}')".format(ID_code, staff, justi, num, date)
            cur.execute(query)
            mysql.connection.commit()
            cur.close()
            flash('ok!')
            return redirect(url_for('GetEmplInfo', ID_code = ID_code))
    staff = GetStaffAndDept()
    return render_template('Employees/createTransfer.html',  Staff = staff, Priviliges = priv)

@app.route('/Project/AddEmplOnProj<int:id>', methods=('GET', 'POST'))
def AddEmplOnProj(id):
    if request.method == 'POST':
        empl = request.form['Employee']
        num = request.form['Number']      

        if not empl:
            flash('Вы не указали работника!')
        cur = mysql.connection.cursor()
        query = "INSERT INTO project_employee (Project, Employee, Salary) VALUES({0}, {1}, {2})".format(id, empl, num)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        flash('ok!')
        return redirect(url_for('GetProjInf', id = id)) 
    empls = GetEmployees()          
    return render_template('Projects/AddEmplOnProj.html', Empls = empls, Priviliges = priv)  

@app.route("/Projects/<int:id><int:ID_code>", methods= ['POST'])
def DeleteFromProj(id, ID_code):
    cur = mysql.connection.cursor()
    query = "DELETE FROM project_employee WHERE (Employee = {0}) AND (Project = {1})".format(ID_code, id)
    cur.execute(query)
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('GetProjInf', id = id))

app.run(debug=True)
