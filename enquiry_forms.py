from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, SelectField, RadioField
from wtforms.validators import (DataRequired, Regexp, ValidationError,
								Email, Length, EqualTo
								)

class JoinDetailsForm(Form):
	Joined_service = SelectField( "Joined Service?", choices=[('1','Yes'),('0','No')],
									 validators = [DataRequired()] )
	Did_not_join_reason = SelectField("Did Not Join Reason", 
										choices=[	('NULL','None'),
													('Distance','Distance'),
													('Time Constraints', 'Time Constraints')
												],
										validators = [DataRequired()])

	comments = TextAreaField("Please add any additional comments")


class LoginForm(Form):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password',validators=[DataRequired()])