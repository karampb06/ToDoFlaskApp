
from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class InfoModel(db.Model):
    __tablename__ = 'info_table' #Name of table in the actual SQL table is 'info_table'
 
    id = db.Column(db.Integer, primary_key = True) # Deciding the column name, its data type, key
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    password = db.Column(db.String())
    gender = db.Column(db.String())
 
    # Constructor of the class
    def __init__(self, name, age, pwd): #Constructor of the class -> InfoModel(string name, int age, string pwd)
        self.name = name #this.name = name
        self.age = age  #this.age = age
        self.password = pwd #this.password = password

    # Constructor of the class
    def __init__(self, name, age, pwd, gender): #Constructor of the class -> InfoModel(string name, int age, string pwd)
        self.name = name #this.name = name
        self.age = age  #this.age = age
        self.password = pwd #this.password = password
        self.gender = gender #this.gender = gender       
 
    # Similar to a ToString() function where we give a string representation of an object
    # when we print it 
    def __repr__(self):
        return f"{self.name}:{self.age}" # if we give a string representation, it only shows the name and age