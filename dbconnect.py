import pypyodbc

cnxn = pypyodbc.connect('Driver={SQL Server Native Client 10.0};'
						'server=DASDB01;'
						'database=IA_ThankQ;'
						'trusted_connection=yes;')

cursor = cnxn.cursor()

cursor.execute("select top 10* from Selections")

row = cursor.fetchone()

if row:
	print(row)
