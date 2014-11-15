from flask.ext.login import UserMixin

class User(UserMixin):		# stores all of our user data
	def __init__(self, username, password, bestFoods):
		self.username = username
		self.password = password
		self.location=(0,0)
		self.bestFoods = bestFoods

	def get_id(self):
		return unicode(self.username)	#flask login ids have to be unicode

	def getFoods(self):
		return self.bestFoods

	def set_name(self,username):
		self.username = username

	def get_name(self):
		return self.username

	def setLocation(self,loc):
		self.location = location

	def getLocation(self):
		return self.location

	

		# favorite foods
		# name
		# college
		# GPS
		# 