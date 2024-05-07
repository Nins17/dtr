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


@app.route("/",methods=["POST", "GET"])
def index():
    current_date = date.today().strftime("%Y-%m-%d")
    return render_template("index.html", date=current_date, time=current_time)

@app.route('/current_time')
def current_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    return jsonify({'current_time': current_time})

@app.route('/current_date')
def current_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    return jsonify({'current_date': current_date})

@app.route('/inam',methods=["POST", "GET"])
def inam():
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
        rfid=request.form['trfid'] 
        
        justcurrent_date = datetime.now().strftime("%Y-%m-%d")
        justcurrent_time = datetime.now().strftime("%H:%M:%S")
       
      
        if rfid in all_rfid:
            if rfid in all_drfid and justcurrent_date in all_date:
                pass
            else:
                cursor.execute('SELECT * FROM employees WHERE rfid=%s',(rfid)) 
                account = cursor.fetchone()
                print(account)
                name =(account[3]+" "+account[4])
                print(account)
                img =account[1]  
            
                query= "INSERT INTO `data`(`rfid`, `img`, `emp_name`, `date`, `time_inAm`, `time_outAm`, `time_inPm`, `time_outPm`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (rfid,img,name,justcurrent_date,justcurrent_time,"-","-","-")
                cursor.execute(query,values)
                conn.commit()
                flash('**Successfully Timed in**', 'success')
         
        else:
            flash('**RFID not found!**', 'error')
           
    cursor.execute('SELECT * FROM data') 
    datas = list(cursor.fetchall())
    
    return render_template("records.html",datas=datas)

@app.route('/inpm',methods=["POST", "GET"])
def inpm():
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
        rfid=request.form['trfid'] 
        
        justcurrent_date = datetime.now().strftime("%Y-%m-%d")
        justcurrent_time = datetime.now().strftime("%H:%M:%S")
       
      
        if rfid in all_rfid:
            if rfid in all_drfid and justcurrent_date in all_date:
                query = "UPDATE data SET time_inPm=%s WHERE rfid=%s and date=%s"
                values = (justcurrent_time,rfid,justcurrent_date)
                cursor.execute(query, values)
                conn.commit()
                
            else:
                cursor.execute('SELECT * FROM employees WHERE rfid=%s',(rfid)) 
                account = cursor.fetchone()
                print(account)
                name =(account[3]+" "+account[4])
                print(account)
                img =account[1]  
            
                query= "INSERT INTO `data`(`rfid`, `img`, `emp_name`, `date`, `time_inAm`, `time_outAm`, `time_inPm`, `time_outPm`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (rfid,img,name,justcurrent_date,"-","-",justcurrent_time,"-")
                cursor.execute(query,values)
                conn.commit()
                flash('**Successfully Timed in**', 'success')
         
        else:
            flash('**RFID not found!**', 'error')
           
    cursor.execute('SELECT * FROM data') 
    datas = list(cursor.fetchall())
    
    return render_template("records.html",datas=datas)

@app.route('/outam',methods=["POST", "GET"])
def outam():
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
        rfid=request.form['trfid'] 
        
        justcurrent_date = datetime.now().strftime("%Y-%m-%d")
        justcurrent_time = datetime.now().strftime("%H:%M:%S")
       
      
        if rfid in all_rfid:
            if rfid in all_drfid and justcurrent_date in all_date:
                query = "UPDATE data SET time_outAm=%s WHERE rfid=%s and date=%s"
                values = (justcurrent_time,rfid,justcurrent_date)
                cursor.execute(query, values)
                conn.commit()
                
            else:
                cursor.execute('SELECT * FROM employees WHERE rfid=%s',(rfid)) 
                account = cursor.fetchone()
                print(account)
                name =(account[3]+" "+account[4])
                print(account)
                img =account[1]  
            
                query= "INSERT INTO `data`(`rfid`, `img`, `emp_name`, `date`, `time_inAm`, `time_outAm`, `time_inPm`, `time_outPm`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (rfid,img,name,justcurrent_date,"-",justcurrent_time,"-","-")
                cursor.execute(query,values)
                conn.commit()
                flash('**Successfully Timed in**', 'success')
         
        else:
            flash('**RFID not found!**', 'error')
           
    cursor.execute('SELECT * FROM data') 
    datas = list(cursor.fetchall())
    
    return render_template("records.html",datas=datas)

@app.route('/outpm',methods=["POST", "GET"])
def outpm():
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
        rfid=request.form['trfid'] 
        
        justcurrent_date = datetime.now().strftime("%Y-%m-%d")
        justcurrent_time = datetime.now().strftime("%H:%M:%S")
       
      
        if rfid in all_rfid:
            if rfid in all_drfid and justcurrent_date in all_date:
                query = "UPDATE data SET time_outPm=%s WHERE rfid=%s and date=%s"
                values = (justcurrent_time,rfid,justcurrent_date)
                cursor.execute(query, values)
                conn.commit()
                
            else:
                cursor.execute('SELECT * FROM employees WHERE rfid=%s',(rfid)) 
                account = cursor.fetchone()
                print(account)
                name =(account[3]+" "+account[4])
                print(account)
                img =account[1]  
            
                query= "INSERT INTO `data`(`rfid`, `img`, `emp_name`, `date`, `time_inAm`, `time_outAm`, `time_inPm`, `time_outPm`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (rfid,img,name,justcurrent_date,"-","-","-",justcurrent_time)
                cursor.execute(query,values)
                conn.commit()
                flash('**Successfully Timed in**', 'success')
         
        else:
            flash('**RFID not found!**', 'error')
           
    cursor.execute('SELECT * FROM data') 
    datas = list(cursor.fetchall())
    
    return render_template("records.html",datas=datas)
       
            
       
            
             
    

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
            department=request.form['dep']		
            
            if rfid in all_rfid:
                flash('**RFID already exist, Sign up again.**', 'error')

            else:
                flash('*Account successfully added!!!!!!*', 'success')
                query = "INSERT INTO employees (id,img,rfid,fname,lname,department ) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (0,img,rfid,fname,lname,department)
                cursor.execute(query, values)
                conn.commit()
           
    
    return render_template("register.html")

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



if __name__ == "__main__":
    app.run(debug=True, port=5001)