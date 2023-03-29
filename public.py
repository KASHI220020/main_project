from flask import *
from database import *
public=Blueprint('public',__name__)

@public.route('/')
def home():

    return render_template('home.html')
@public.route('/login',methods=['post','get'])
def login():
    if 'submit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        print(fname,lname)
        q="select * from login where username='%s' and password='%s'"%(fname,lname)
        res=select(q)
        if res:
            if res[0]['usertype']=="admin":
                return redirect(url_for("admin.adminhome"))
    return render_template('login.html')

@public.route('/reg',methods=['post','get'])
def reg():
    if 'submit' in request.form:
        name=request.form['name']    
        lname=request.form['lname']
        number=request.form['number']
        email=request.form['email']
        place=request.form['place']
        pin=request.form['pin']
        gender=request.form['gender']
        uname=request.form['uname']
        psw=request.form['psw']
        q="insert into login values(null,'%s','%s','agent')"%(uname,psw)
        ids=insert(q)
        q="insert into agent values(null,'%d','%s','%s','%s','%s','%s','%s','%s')"%(ids,name,lname,gender,place,pin,email,number)
        insert(q)
        
    return render_template('reg.html')