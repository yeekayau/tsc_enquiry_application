from flask.ext.login import UserMixin


class User(UserMixin):
	def __init__(self, userid, username, active=True):
		self.userid = userid
		self.username = username
		self.active = active

	def is_active(self):
		return self.active

	def is_anonymous(self):
		return False

	def is_authenticated(self):
		return True

	def get_id(self):
		return self.userid