from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/sample"
mongo =PyMongo(app)
# Dummy user database
#users = {'username': 'password'}

@app.route('/',methods=["GET","POST"])
def home():
    
    if request.method=='POST':
        name=request.form['name']
        phone_no=request.form['phone']
        email=request.form['email']
        password=request.form['password']
        
        mongo.db.user.insert_one({"name":name,"phone_no":phone_no,"email":email,"password":password})
        return render_template('home.html')
    return render_template('home.html')

@app.route('/register')
def register():
   
    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    # if request.method=="GET":
        # password=request.form["password"] 
        # python app.py
        # name=request.form["name"] 
        
        return render_template('login.html')
        

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
   
    return render_template('login.html')

@app.route('/about',methods=['GET','POST'])
def about():
   
    return render_template('about.html')







if __name__ == '__main__':
    app.run(debug=True)