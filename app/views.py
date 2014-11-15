from flask import render_template, request, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from app import app, login_manager
from forms import RegisterForm, LoginForm
from flask.ext.login import current_user, login_user, logout_user, login_required
from models import User
from pymongo import MongoClient

client = MongoClient('mongodb://norfrosh:food@ds051110.mongolab.com:51110/users')
db = client.users
user = db.user

@login_manager.user_loader
def load_user(userid):
	u = user.find_one({"username": userid})
	bestFoods = {}
	for food in r['firstFoods']:
		bestFoods[food]=10
	for food in r['secondFoods']:
		bestFoods[food] = 7
	for food in r['thirdFoods']:
		bestFoods[food] = 4
	return User(userid, r['password'], bestFoods) 


@app.route('/')
def index():
	form = LoginForm()
	return render_template('index.html', user=current_user, login_form = form)

@app.route('/register', methods=['GET','POST'] )
def register():
	form = RegisterForm()
	if request.method == 'POST':
		bestFoods = {}
		for food in form.firstFoods.data:
			bestFoods[food]=10
		for food in form.secondFoods.data:
			bestFoods[food] = 7
		for food in form.thirdFoods.data:
			bestFoods[food] = 4
		user_data = {
			'name': form.username.data,
			'password': generate_password_hash(form.password.data),
			'foodList': bestFoods
		}
		user.insert(user_data)

		return redirect(url_for('index'))

	return render_template('register.html', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
	form = LoginForm()
	u = user.find_one({"username": form.username.data})
	print u
	print "trying to login"
	if u: # and check_password_hash(user['password'], form.password.data):
		print 'should be logging in now'
		uu = load_user(form.teamname.data)
		login_user(uu)
	return redirect(url_for('index'))

@app.route('/getloc',methods=['POST'])
@login_required
def getloc():

	print request.form["lat"], request.form["lng"]
	return request.form["lat"], request.form["lng"]

@app.route('/logout', methods=["POST"])
def logout():
	logout_user()
	return redirect(url_for('index'))