from flask.ext.login import UserMixin

class User(UserMixin):		# stores all of our user data
	def __init__(self, teamname, names, languages, email, password):
		self.teamname = teamname
		self.name = names
		self.languages = languages
		self.email = email
		self.password = password
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

	def set_xlocation(x):
		self.x = x

	def get_xlocation():
		return self.x

	def set_ylocation(y):
		self.y = y

	def get_ylocation():
		return y

	

		# favorite foods
		# name
		# college
		# GPS
		# 