from flask import (Flask, g, render_template, flash, redirect, url_for)
import pypyodbc


DEBUG=True

# create instance of a Flask app
app = Flask(__name__)

# ----------------------------------------
# Create connection to DB
cnxn = pypyodbc.connect('Driver={SQL Server Native Client 10.0};'
						'server=DASDB01;'
						'database=IA_CDIS;'
						'trusted_connection=yes;'
						'MARS_Connection=yes;')

cursor = cnxn.cursor()
cursor.execute('select * from Enquiries')


@app.route('/')
def index():
	enquiry_list = []
    
	cursor = cnxn.cursor()
	cursor.execute('select * from Enquiries')
	
	for row in cursor.fetchall():
		enquiry_dict = dict(id = row[0], date = row[3], firstname = row[9])
		enquiry_list.append(enquiry_dict)
	
	return render_template('index.html', rows = enquiry_list)
	


if __name__ == '__main__':
    app.run(debug=DEBUG)