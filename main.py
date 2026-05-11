from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import database_model
from database import session, engine
from flask import Flask, render_template

app = FastAPI()
app1 = Flask(__name__)
#the below line will create tables on its own 
database_model.Base.metadata.create_all(bind = engine)
    #metadatawill all the info about the talbe, columns, data types etc
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://127.0.0.1:5500/index.html"],
    allow_methods = ["*"]
)

@app.get("/")
def greet():
    return "Welcome to the server"

def get_db():
    db = session() # crearing the db
    try:
        yield db        #waiting for others to use it 
    finally:
        db.close()      #then closing the db

@app.get("/login/{emil_id}/{password}")
def readlogin(email_id : str, password : str, db : Session = Depends(get_db)):
    db_info = db.query(database_model.login_info).filter(database_model.login_info.email_id == email_id, database_model.login_info.password == password).first()
    if(db_info):
        dashboard()
    else:
        return "Username or Password wrong" 

@app1.route("/mydashboard")
def dashboard():
    return render_template('mydashboard.html')

@app.post("/registration/{name}/{phone}/{email_id}/{password}")
def newlogin(name : str, phone : int, email_id : str, password : str, db : Session = Depends(get_db)):
    #db.add(database_model.login_info(name, phone, email_id, password)) --> this is synatically correct but then in the future if we change order of the columns then it breaks silently 
    new_registration = database_model.login_info(
    name=name, 
    phone=phone,                                    # --> this is more reliable way of alternativly writing the above line of code 
    email_id=email_id, 
    password=password
    )
    db.add(new_registration)
    db.commit() 
    return "Resitration successfully"

