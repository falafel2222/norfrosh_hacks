from flask import render_template, request, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from app import app, login_manager
from forms import RegisterForm, LoginForm
from flask.ext.login import current_user, login_user, logout_user
from models import User

@login_manager.user_loader
def load_user(userid):
	#r = firebase.get('/users/'+ userid + '.json')
	r = {} # update to get user from mongodb
	pass #User(userid, r['names'], r['languages'], r['email'], r['password']) 


@app.route('/')
def index():
	form = LoginForm()
	return render_template('index.html', user=current_user, login_form = form)

@app.route('/register', methods=['GET','POST'] )
def register():
	form = RegisterForm()
	if request.method == 'POST':
		user_data = {
			'names': form.names.data,
			'languages': form.languages.data,
			'email': form.email.data,
			'password': generate_password_hash(form.password.data)
		}
		teamname = form.teamname.data
		#firebase.put('/users/'+teamname+'.json',user_data)

		return redirect(url_for('index'))

	return render_template('register.html', form=form)

@app.route('/login', methods=['POST'])
def login():
	form = LoginForm()
	#user = firebase.get('/users/'+form.teamname.data + '.json')
	user = null
	print user
	print "trying to login"
	if user: # and check_password_hash(user['password'], form.password.data):
		print 'should be logging in now'
		u = load_user(form.teamname.data)
		login_user(u)
	return redirect(url_for('index'))

@app.route('/logout', methods=["POST"])
def logout():
	logout_user()
	return redirect(url_for('index'))
