from flask import (Flask, g, render_template, flash, redirect, url_for)
import pypyodbc


DEBUG=True

# create instance of a Flask app
app = Flask(__name__)

# ----------------------------------------
# Create connection to DB, the Mars_Connection thing allows you to fetch multiple rows
cnxn = pypyodbc.connect('Driver={SQL Server Native Client 10.0};'
						'server=DASDB01;'
						'database=IA_CDIS;'
						'trusted_connection=yes;'
						'MARS_Connection=yes;')


@app.route('/')
def index():

	enquiry_list = []
    
	cursor = cnxn.cursor()
	cursor.execute('select * from Enquiries')
	
	# cursor fetchall() retrieves a list of tuples
	for row in cursor.fetchall():
		enquiry_dict = dict(enq_id = row[0], enq_date = row[3], firstname = row[9],
							lastname = row[10],
							dateofbirth = row[11],
							relationship_to_child = row[14],
							caregiver_firstname = row[12],
							caregiver_lastname = row[13]
							)
		enquiry_list.append(enquiry_dict)

	return render_template('index.html', rows=enquiry_list)
	
@app.route('/enquiry/<int:enq_id>')
def view_enq(enq_id):
	enquiry_list = []
	cursor = cnxn.cursor()
	cursor.execute("""select * from Enquiries where enquiry_id = ?""", [str(enq_id)] )

	for row in cursor.fetchall():
		enquiry_dict = dict(enq_id = row[0], enq_date = row[3], firstname = row[9],
							lastname = row[10],
							dateofbirth = row[11],
							relationship_to_child = row[14],
							caregiver_firstname = row[12],
							caregiver_lastname = row[13]
							)
		enquiry_list.append(enquiry_dict)
	
	return render_template('view_enquiry.html', enquiry=enquiry_list)	


if __name__ == '__main__':
    app.run(debug=DEBUG)