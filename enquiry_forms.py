from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import (DataRequired, Regexp, ValidationError,
								Email, Length, EqualTo
								)

class JoinDetailsForm(Form):
	Did_not_Join_reason = SelectField(u'Did Not Join Reason', 
										choices=[('Too Far','Distance'),
												('Time is not good', 'Time Constraints')
												],
										validators = DataRequired())

	comments = TextAreaField("Please add any comments", 
								validators = [DataRequired()])