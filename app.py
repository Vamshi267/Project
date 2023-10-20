import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
import sqlite3
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
import pandas as pd
import numpy as np
import pickle
import sqlite3
import random

import smtplib 
from email.message import EmailMessage
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    #int_features= [float(x) for x in request.form.values()]
    val1, val2, val3, val4, val5, val6, val7,val8 = (request.form['0']),(request.form['1']), float(request.form['2']), float(request.form['3']), float(request.form['4']), float(request.form['5']), float(request.form['6']), float(request.form['7'])
    final1 = np.array([val3,val4,val5,val6,val7,val8]).reshape(1,-1)
    #final2 = np.array([val6,val7,val8]).reshape(1,-1)
    
    model = joblib.load("model.sav")
    predict = model.predict(final1)
    predict = predict[0]
    

    return render_template('result.html', output=round(predict,2))



@app.route('/logon')
def logon():
	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('signin.html')


@app.route("/signup")
def signup():
    global otp, username, name, email, number, password
    username = request.args.get('user','')
    name = request.args.get('name','')
    email = request.args.get('email','')
    number = request.args.get('mobile','')
    password = request.args.get('password','')
    otp = random.randint(1000,5000)
    print(otp)
    msg = EmailMessage()
    msg.set_content("Your OTP is : "+str(otp))
    msg['Subject'] = 'OTP'
    msg['From'] = "evotingotp4@gmail.com"
    msg['To'] = email
    
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("evotingotp4@gmail.com", "xowpojqyiygprhgr")
    s.send_message(msg)
    s.quit()
    return render_template("val.html")

@app.route('/predict1', methods=['POST'])
def predict1():
    global otp, username, name, email, number, password
    if request.method == 'POST':
        message = request.form['message']
        print(message)
        if int(message) == otp:
            print("TRUE")
            con = sqlite3.connect('signup.db')
            cur = con.cursor()
            cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`) VALUES (?, ?, ?, ?, ?)",(username,email,password,number,name))
            con.commit()
            con.close()
            return render_template("signin.html")
    return render_template("signup.html")

@app.route("/signin")
def signin():

    mail1 = request.args.get('user','')
    password1 = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("signin.html")    

    elif mail1 == str(data[0]) and password1 == str(data[1]):
        return render_template("index.html")
    else:
        return render_template("signin.html")


@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/notebook1')
def notebook1():
	return render_template('static/Aegean/SKG_AMS.html')

@app.route('/notebook2')
def notebook2():
	return render_template('static/Aegean/SKG_ARN.html')

@app.route('/notebook3')
def notebook3():
	return render_template('static/Aegean/SKG_BRU.html')


@app.route('/notebook4')
def notebook4():
	return render_template('static/Aegean/SKG_CDG.html')

@app.route('/notebook5')
def notebook5():
	return render_template('static/Aegean/SKG_LIS.html')

@app.route('/notebook6')
def notebook6():
	return render_template('static/Aegean/SKG_VIE.html')

@app.route('/notebook7')
def notebook7():
	return render_template('static/Austrian/SKG_AMS.html')

@app.route('/notebook8')
def notebook8():
	return render_template('static/Austrian/SKG_ARN.html')

@app.route('/notebook9')
def notebook9():
	return render_template('static/Austrian/SKG_BRU.html')


@app.route('/notebook10')
def notebook10():
	return render_template('static/Austrian/SKG_CDG.html')

@app.route('/notebook11')
def notebook11():
	return render_template('static/Austrian/SKG_LIS.html')

@app.route('/notebook12')
def notebook12():
	return render_template('static/Austrian/SKG_VIE.html')


@app.route('/notebook13')
def notebook13():
	return render_template('static/Lufthansa/SKG_AMS.html')

@app.route('/notebook14')
def notebook14():
	return render_template('static/Lufthansa/SKG_ARN.html')

@app.route('/notebook15')
def notebook15():
	return render_template('static/Lufthansa/SKG_BRU.html')


@app.route('/notebook16')
def notebook16():
	return render_template('static/Lufthansa/SKG_CDG.html')

@app.route('/notebook17')
def notebook17():
	return render_template('static/Lufthansa/SKG_LIS.html')

@app.route('/notebook18')
def notebook18():
	return render_template('static/Lufthansa/SKG_VIE.html')

@app.route('/notebook19')
def notebook19():
	return render_template('static/Turkish/SKG_AMS.html')

@app.route('/notebook20')
def notebook20():
	return render_template('static/Turkish/SKG_ARN.html')

@app.route('/notebook21')
def notebook21():
	return render_template('static/Turkish/SKG_BRU.html')


@app.route('/notebook22')
def notebook22():
	return render_template('static/Turkish/SKG_CDG.html')

@app.route('/notebook23')
def notebook23():
	return render_template('static/Turkish/SKG_LIS.html')

@app.route('/notebook24')
def notebook24():
	return render_template('static/Turkish/SKG_VIE.html')


@app.route('/notebook25')
def notebook25():
	return render_template('static/SecndExp/Aegean.html')


@app.route('/notebook26')
def notebook26():
	return render_template('static/SecndExp/Austrian.html')

@app.route('/notebook27')
def notebook27():
	return render_template('static/SecndExp/Lufthansa.html')

@app.route('/notebook28')
def notebook28():
	return render_template('static/SecndExp/Turkish.html')



if __name__ == "__main__":
    app.run()
