from flask import Flask,render_template,request,session,redirect,url_for
import mysql.connector
import  re
from datetime import timedelta


atm_o=Flask(__name__)
atm_o.secret_key="my secret key"
db_connctr=mysql.connector.connect(host="localhost",user="root",password="root",database="atm_4546")
cursr=db_connctr.cursor()  #cursor point

atm_o.permanent_session_lifetime=timedelta(minutes=5)

@atm_o.route("/")
def welcome():
    if  "username" in session:
        return  redirect(url_for("home"))
    elif "ac_no" in session:
        return redirect(url_for("pin")) 
    return render_template("welcome.html")

@atm_o.route("/ac_details",methods=["GET","POST"])
def ac_no():
    if session:
        return redirect(url_for("home"))
       
    if request.method=="POST":
        ac_no=request.form["ac_no"]  #1234 1234 1234
        pattern=r"^\d{4} \d{4} \d{4}$"
        if not re.match(pattern,ac_no):
            return render_template("account.html",info="*plz enter valid ac_no \n like XXXX XXXX XXXX ")
        else:
            cursr.execute("""select ac_no,pin from user_data where ac_no=%s;""",(ac_no,))

            data=cursr.fetchone() #
            if data:
                session.permanent=True
                session["ac_no"]=data[0]
                session["pin"]=data[1]

                return  redirect(url_for("pin"))
            else:

               return render_template("account.html",info="* The ac_no is un-identified  ")



    return render_template("account.html")

@atm_o.route("/pin",methods=["GET","POST"])
def pin():  
    if  "ac_no" not in session:
        return  redirect(url_for("ac_no"))
    elif "username" in session:
        return redirect(url_for("home")) 
    
    if request.method=="POST":
        if request.form["password"]=="password":
            acc_no=session.get("ac_no")
            pin=request.form["pin"]
            if int(pin)== int(session.get("pin")):
                cursr.execute(""" select u_name from user_data where ac_no=%s;""",(acc_no,))
                data=cursr.fetchone()
                session["username"]=data[0]
                
                return redirect(url_for("home"))
            else :
                return render_template("pin.html",info="*incorrect pin")


    return render_template("pin.html")

@atm_o.route("/home")
def home():
    if "ac_no" not in session:
        return redirect(url_for("ac_no"))
    
    elif "username" not in session:
        return redirect(url_for("pin"))
    
    return render_template("home.html",username=session.get("username"))

@atm_o.route("/check_balance")
def check_balance():
    if "ac_no" not in session:
        return redirect(url_for("ac_no"))
    
    elif "username" not in session:
        return redirect(url_for("pin"))
    ac_no=session.get("ac_no")
    cursr.execute("""select balance from user_data where ac_no=%s; """,(ac_no,))
    data=cursr.fetchone()
    if data:
        return render_template("balance.html",username=session.get("username"),balance=data[0])



@atm_o.route("/desposite" , methods=["GET","POST"])
def deposite():
    if "ac_no" not in session:
        return redirect(url_for("ac_no"))
    
    elif "username" not in session:
        return redirect(url_for("pin"))
    
    if request.method == "POST":
        ac_no=session.get("ac_no")
        d_amount=request.form["d_amount"]
        cursr.execute(""" update user_data  set balance = balance + %s where ac_no=%s;""",(d_amount,ac_no))
        db_connctr.commit()

        cursr.execute("""select balance from user_data where ac_no=%s; """,(ac_no,))
        data=cursr.fetchone()

        return render_template("notification_d.html",username=session.get("username"),balance=data[0])


    return render_template("deposite.html")



@atm_o.route("/logout")
def logout():
    if "username" not in session:
        return  redirect(url_for("ac_no"))

    session.clear()
    return redirect(url_for("welcome"))

  



if __name__=="__main__":
    atm_o.run(debug=True,port=5003)