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
						'trusted_connection=yes;')

cursor = cnxn.cursor()

cursor.execute('select * from Enquiries')

rows = cursor.fetchall()


@app.route('/')
def index():
	return render_template('index.html')
	


if __name__ == '__main__':
    app.run(debug=DEBUG)