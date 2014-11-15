from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash
from app import app, login_manager
from forms import RegisterForm, LoginForm
from flask.ext.login import current_user, login_user, logout_user, login_required
from models import User
from pymongo import MongoClient
import algorithm

client = MongoClient('mongodb://norfrosh:food@ds051110.mongolab.com:51110/users')
db = client.users
user = db.user

@login_manager.user_loader
def load_user(userid):
	print userid
	u = user.find_one({"name":userid})
	if u:
		return User(userid, u['password'],u['foodList']) 


@app.route('/')
def index():
	return render_template('index.html', user=current_user)

@app.route('/choice')
def choice():
	choice, hall = algorithm.makeChoice(current_user.getLocation(), current_user.getFoods())
	
	return render_template('choice.html',choice=choice,hall=hall,user=current_user)

@app.route('/register', methods=['GET','POST'] )
def register():
	form = RegisterForm()
	if request.method == 'POST':
		bestFoods = {}
		for food in form.firstFoods.data:
			bestFoods[food]=10.0
		for food in form.secondFoods.data:
			bestFoods[food] = 7.0
		for food in form.thirdFoods.data:
			bestFoods[food] = 4.0
		user_data = {
			'name': form.username.data,
			'password': generate_password_hash(form.password.data),
			'foodList': bestFoods
		}
		user.insert(user_data)

		return redirect(url_for('index'))

	return render_template('register.html', form=form, user=current_user)

@app.route('/login', methods=['POST', 'GET'])
def login():
	form = LoginForm()
	if request.method == 'GET':
		return render_template('login.html', login_form=form, user= current_user)
	u = user.find_one({"name": form.username.data})
	#print u
	if u:
		print 'should be logging in now'
		uu = load_user(form.username.data)
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
	flash('Logged out successfully.', 'success')
	return redirect(url_for('index'))

