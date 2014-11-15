from flask.ext.login import UserMixin

class User(UserMixin):		# stores all of our user data
	def __init__(self, teamname, names, languages, email, password):
		self.teamname = teamname
		self.names = names
		self.languages = languages
		self.email = email
		self.password = password
	def get_id(self):
		return unicode(self.teamname)	#flask login ids have to be unicode