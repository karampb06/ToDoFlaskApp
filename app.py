from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask,render_template,request, redirect
from models import db, InfoModel

from flask import Flask
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Cellfone01@localhost:5432/flaskdemodb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db.init_app(app)
migrate = Migrate(app, db)
 
#general Flask Code
@app.route('/', methods=['GET'])
def index():
    #userdata = Users.query.all()
    #usersdata = db.session.execute(db.select(Users).order_by(Users.id)).scalars()
    return render_template('home.html')


@app.route('/registeruser', methods=['GET', 'POST'])
def registeruser():

    if request.method == "POST":

        # get user data
        full_name_data = request.form['fullname']
        age_data = request.form['age']
        password_data = request.form['password']
        gender_data = request.form['gender']

        # populate database
        # newUser = InfoModel(name=full_name_data, age=age_data, pwd=password_data)
        newUser = InfoModel(name=full_name_data, age=age_data, pwd=password_data, gender=gender_data)
        db.session.add(newUser)
        db.session.commit()

        # usersdata = db.session.execute(db.select(Users).order_by(Users.id)).scalars()
        # return render_template('users.html', usersdata=usersdata)
        return render_template('home.html')
        #return "<h4>User created</h4>"
    return render_template('register.html')

@app.route('/edit-user/<int:user_id>', methods=['GET','POST'])
def edit_user(user_id):
	# Get the details of the user to edit from the request parameter user_id
	user_obj_to_edit = db.session.execute(db.select(InfoModel).filter_by(id=user_id)).scalar_one()

	if user_obj_to_edit: # If the user of the specified id still exists then do the following
		if request.method == "POST":
			# get posted user data from the form
			full_name_data = request.form['full_name']
			age_data = request.form['age']
			gender_data = request.form['gender']

			#update the user object to edit with the new values from the form
			user_obj_to_edit.name = full_name_data
			user_obj_to_edit.age = age_data
			user_obj_to_edit.gender = gender_data

			db.session.commit() #finalize the database update
			return redirect('/all-users-list')

		elif request.method == "GET":
			# pass the user object to edit to the template for edit form
			# this is done to load the edit form with the data of this user object
			print(user_obj_to_edit)
			return render_template("edit_user.html", user_data = user_obj_to_edit)
	else: # if the user of the specified id does not exist anymore, then return the following message
		return "<h4>Sorry, the selected user does not exist anymore in the system!</h4>"
		

@app.route('/all-users-list', methods=['GET'])
def view_all_users():
   
    users_data = InfoModel.query.all()
    #users_data = db.session.execute(db.select(Users).order_by(Users.id)).scalars()
    return render_template('users_list.html', users_data=users_data)
 
if __name__ == '__main__':
    app.run(debug=True)