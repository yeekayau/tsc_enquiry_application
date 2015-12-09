from flask import (Flask, g, render_template, flash, redirect, url_for)
from flask.ext.login import (LoginManager, login_user, logout_user,
								login_required, current_user)

import pypyodbc

import enquiry_forms
from enquiry_models import User


DEBUG=True

# create instance of a Flask app
app = Flask(__name__)
app.secret_key = 'dhfgq8fg2379tfrgo2iefbhwdcfuwef2i3t9723fgiw'

# ----------------------------------------
# Create connection to DB, the Mars_Connection thing allows you to fetch multiple rows
cnxn = pypyodbc.connect('Driver={SQL Server Native Client 10.0};'
						'server=DASDB01;'
						'database=IA_CDIS;'
						'trusted_connection=yes;'
						'MARS_Connection=yes;')

#Create new instance of LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
	cursor = cnxn.cursor()
	cursor.execute("""
					select UserID, Username
					from ApplicationUsers
					where UserID = ?""", [str(userid)])
	rows = cursor.fetchall()
	if rows:
		for field in rows:
			userid = field[0]
			username = field[1]
			print(userid)
			print(username)
			user = User(userid, username) #creates an instance of a user
		return user
	else:
		return None	


@app.route('/', methods=['GET','POST'])
def login():
	form = enquiry_forms.LoginForm()
	
	if form.validate_on_submit():
		cursor = cnxn.cursor()
		cursor.execute("""
					select UserID, Username
					from ApplicationUsers
					where Username = ? and Password = ? """, 
					(form.username.data, form.password.data) )
		rows = cursor.fetchall()
		if rows:
			for field in rows:
				userid = field[0]
				username = field[1]
				print(userid)
				print(username)
				user = User(userid, username)
				login_user(user)
				flash("You have logged in!", "success")
			return redirect(url_for('index'))
		else:
			flash("You email or password is incorrect", "error")
	return render_template('login.html', form=form)


@app.route('/index')
def index():

	enquiry_list = []
    
	cursor = cnxn.cursor()
	cursor.execute('select * from Enquiries order by '
		'date_finish desc')
	
	# cursor fetchall() retrieves a list of tuples
	for row in cursor.fetchall():
		enquiry_dict = dict(enq_id = row[0], enq_date = row[3], firstname = row[9],
							lastname = row[10],
							dateofbirth = row[11],
							relationship_to_child = row[14],
							caregiver_firstname = row[12],
							caregiver_lastname = row[13],
							caregiver_phone = row[17],
							caregiver_alt_phone = row[18],
							caregiver_email = row[19]
							)
		enquiry_list.append(enquiry_dict)

	return render_template('index.html', rows=enquiry_list)
	
@app.route('/enquiry/<int:enq_id>', methods=('GET','POST'))
def view_enq(enq_id):

	enquiry_list = []
	cursor = cnxn.cursor()
	# the variable provided needs to be a list
	cursor.execute("""select * from Enquiries where enquiry_id = ?""", [str(enq_id)] )

	for row in cursor.fetchall():
		enquiry_dict = dict(enq_id = row[0], enq_date = row[3], firstname = row[9],
							lastname = row[10],
							dateofbirth = row[11],
							relationship_to_child = row[14],
							caregiver_firstname = row[12],
							caregiver_lastname = row[13],
							caregiver_phone = row[17],
							caregiver_alt_phone = row[18],
							caregiver_email = row[19],
							preferred_contact_method = row[20],
							p_c_day_mon_morning = row[21],
							p_c_day_mon_lunch = row[22],
							p_c_day_mon_afternoon = row[23],
							p_c_day_tues_morning = row[24],
							p_c_day_tues_lunch = row[25],
							p_c_day_tues_afternoon = row[26],
							p_c_day_wed_morning = row[27],
							p_c_day_wed_lunch = row[28],
							p_c_day_wed_afternoon = row[29],
							p_c_day_thurs_morning = row[30],
							p_c_day_thurs_lunch = row[31],
							p_c_day_thurs_afternoon = row[32],
							p_c_day_fri_morning = row[33],
							p_c_day_fri_lunch = row[34],
							p_c_day_fri_afternoon = row[35],
							how_we_can_help = row[36],
							joined_program = row[37],
							not_joined_reason = row[38],
							comments = row[39]
							)
		enquiry_list.append(enquiry_dict)
	
	form = enquiry_forms.JoinDetailsForm()
	if form.validate_on_submit():
		flash("Details Saved!", "success")
		joined_service = form.Joined_service.data
		did_not_join_reason = form.Did_not_join_reason.data
		comments = form.comments.data

		cursor.execute("""
							update Enquiries
							set joined_program = ?, not_joined_reason = ?,
							comments = ?
							where enquiry_id = ?

							 """, (joined_service, did_not_join_reason,
							 		comments, enq_id) )
		cnxn.commit()


	# You can pass in any python object to a template
	return render_template('view_enquiry.html', enquiry=enquiry_list, form=form)	


if __name__ == '__main__':
    app.run(debug=DEBUG)