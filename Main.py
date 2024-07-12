from flask import Flask, render_template,redirect,url_for, request
from flaskext.mysql import MySQL
from flask import Flask, jsonify
from flask import *
import os
from datetime import date
from datetime import datetime


app = Flask(__name__)
app.secret_key = "santi"
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'  # Database user
app.config['MYSQL_DATABASE_PASSWORD'] = ''  # Database password
app.config['MYSQL_DATABASE_DB'] = 'ppes'  # Name of database
app.config['MYSQL_DATABASE_HOST'] = 'localhost'  # Hosting site
app.config['UPLOAD_FOLDER'] = 'static/assets/pics'

mysql.init_app(app)  
conn = mysql.connect()  
cursor = conn.cursor()


@app.route("/user",methods=["POST", "GET"])
def index():
    current_date = date.today().strftime("%Y-%m-%d")
    return render_template("land.html", date=current_date, time=current_time)

@app.route('/current_time')
def current_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    return jsonify({'current_time': current_time})

@app.route('/current_date')
def current_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    return jsonify({'current_date': current_date})

@app.route('/lgin',methods=["POST", "GET"])
def lgin():
    cursor.execute('SELECT * FROM employees') 
    data = cursor.fetchall() 
    all_rfid = [] 
    for i in data:
        all_rfid.append(i[2])
        print(all_rfid)
        
    cursor.execute('SELECT * FROM data') 
    datas = cursor.fetchall() 
    all_date = []
    all_drfid = [] 
    for i in datas:
        all_date.append(i[4])
        all_drfid.append(i[1])
        
        
    if request.method == "POST":
        rfid=request.form['id'] 
        
        justcurrent_date = datetime.now().strftime("%Y-%m-%d")
        justcurrent_time = datetime.now().strftime("%H:%M:%S")
        cursor.execute('SELECT * FROM employees WHERE rfid=%s', (rfid)) 
        account = cursor.fetchone()
        
    
        if account:  # Check if account is not None
            print(account)
            name = account[3] + " " + account[5]
            print(account)
            img = account[1] 
            shift = account[4]
            dep = account[6]
            
           
            
            if rfid in all_rfid:
                cursor.execute('SELECT * FROM data WHERE rfid=%s and date=%s',(rfid,justcurrent_date)) 
                datas = cursor.fetchone()
               
                
                    
                if datas :
                    daTe=datas[4]
                    timeout=datas[7]
                    timein=datas[6]
                
                    
                    if timein!="-" and timeout=="-":
                        query = "UPDATE data SET time_out=%s WHERE rfid=%s and date=%s"
                        values = (justcurrent_time,rfid,justcurrent_date)
                        cursor.execute(query, values)
                        conn.commit()
                        res="success"
                        flash('**Successfully Timed out', 'success')
                        return render_template("land.html",timeout=timeout,daTe=" on "+ daTe,name=name,shift=shift,img=img,dep=dep,res=res,account=account)
                    
                    elif timein=="-" and timeout!="-":
                            res="danger"
                            flash('**Arlready timed out at ', 'success')
                            return render_template("land.html",timeout=timeout,daTe="but no time in",name=name,shift=shift,img=img,dep=dep,res=res,account=account)
                    elif timein!="-" and timeout!="-":
                            res="danger"
                            flash('**Arlready timed out at ', 'success')
                            return render_template("land.html",timeout=timeout,daTe=" on "+ daTe,name=name,shift=shift,img=img,dep=dep,res=res,account=account)
                    else:
                        query = "UPDATE data SET time_in=%s WHERE rfid=%s and date=%s"
                        values = (justcurrent_time,rfid,justcurrent_date)
                        cursor.execute(query, values)
                        conn.commit()
                        res="success"
                        flash('**Successfully Timed out', 'success')
                        return render_template("land.html",timeout=timeout,daTe=" on "+ daTe,name=name,shift=shift,img=img,dep=dep,res=res,account=account)
                    
               
                else:
                    query= "INSERT INTO `data`(`rfid`, `img`, `emp_name`, `date`, `shift`,`time_in`, `time_out`) VALUES ( %s, %s, %s, %s, %s, %s, %s)"
                    values = (rfid,img,name,justcurrent_date,shift,justcurrent_time,"-")
                    cursor.execute(query,values)
                    conn.commit()
                    res="success"
                    flash('**Successfully Timed in', 'success')
                    return redirect('/user')
              
            else:
                res="danger"
                flash('**RFID not found!**', 'error')
                return render_template("land.html",res=res,account=account)
   
        else:
            res="danger"
            flash('**No account found for the provided RFID!**', 'error')
            return render_template("land.html",res=res,account=account)
    
        
            
             
@app.route("/loginAdmin",methods=["POST", "GET"])
def loginAdmin():
    if request.method == "POST":
        session['username']=request.form['an']
        session['passwrd']=request.form['apass']
        
        cursor.execute('SELECT * FROM admin WHERE username=%s and password=%s',(session['username'],session['passwrd'])) 
        account = cursor.fetchone() 
        
        if account:
            flash('**Welcome to PPES Admin!**', 'success')
            return render_template("index.html")
        else:
            flash('*No Admin Account Found **', 'error')
            return render_template("adminland.html")
            
        

@app.route("/register",methods=["POST", "GET"])
def register():
    if request.method == "POST":
        cursor.execute('SELECT * FROM employees') 
        accounts = cursor.fetchall() 
        all_rfid = []  
        for i in accounts:
            all_rfid.append(i[2]) 
        print(all_rfid)
        file = request.files['pic'] 
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            
            img="static/assets/pics/" + file.filename	
            rfid=request.form['rfid']	
            fname=request.form['fn']		
            lname=request.form['ln']	
            shift=request.form['shift']		
            department=request.form['dep']		
            
            if rfid in all_rfid:
                res="danger"
                flash('**RFID already exist, Sign up again.**', 'error')
                return render_template("register.html",res=res)

            else:
                res="success"
                flash('*Account successfully added!!!!!!*', 'success')
                query = "INSERT INTO employees (id,img,rfid,fname,shift,lname,department ) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (0,img,rfid,fname,shift,lname,department)
                cursor.execute(query, values)
                conn.commit()
                return render_template("register.html",res=res)
        else:
            res="danger"
            flash('**cannot read the file**', 'error')
            return render_template("register.html",res=res)
    else:
        return render_template("register.html")
           
           
    
    

@app.route("/",methods=["POST", "GET"])
def admin():
    cursor.execute('SELECT * FROM data') 
    datas = list(cursor.fetchall())
    
    return render_template("adminland.html",datas=datas)

@app.route("/adminpg",methods=["POST", "GET"])
def adminpg():
    flash('**Welcome to PPES Admin!**', 'success')
    return render_template("index.html")


@app.route("/records",methods=["POST", "GET"])
def records():
    cursor.execute('SELECT * FROM data') 
    datas = list(cursor.fetchall())
    
    return render_template("records.html",datas=datas)

@app.route("/empL",methods=["POST", "GET"])
def emp_list():
    cursor.execute('SELECT * FROM employees') 
    accounts = list(cursor.fetchall())
    
    return render_template("emp_list.html", accounts = accounts)

@app.route('/sign_out')
def sign_out():
    session.clear()
    flash('you have been logged out', 'success')
    return redirect(url_for('admin'))

if __name__ == "__main__":
    app.run(debug=True, port=5001)