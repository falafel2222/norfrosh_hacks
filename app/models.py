from flask.ext.login import UserMixin

class User(UserMixin):		# stores all of our user data
	def __init__(self, username, password, bestFoods):
		self.username = username
		self.password = password
		self.location=(0,0)
		self.bestFoods = bestFoods

	def get_id(self):
		return unicode(self.teamname)	#flask login ids have to be unicode

	def set_name(userName):
		self.name = userName

	def get_name():
		return self.name

	def set_americanFav(L):
		self.american = L

	def get_americanFav():
		return self.american

	def set_italianFav(L):
		self.italian = L

	def get_italianFav():
		return self.italian

	def set_asianFav(L):
		self.asian = L

	def get_asianFav():
		return self.asian

	def set_mexicanFav(L):
		self.mexican = L

	def get_mexicanFav():
		return self.mexican

	def set_mediterranean(L):
		self.mediterranean = L

	def get_mediterranean():
		return self. mediterranean

	def set_college(S):
		self.college = S

	def get_college():
		return self.college

	def set_location(loc):
		self.loc = loc

	def get_location():
		return self.x

	

		# favorite foods
		# name
		# college
		# GPS
		# 