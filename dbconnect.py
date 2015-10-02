import pypyodbc

cnxn = pypyodbc.connect('Driver={SQL Server Native Client 10.0};'
						'server=DASDB01;'
						'database=IA_ThankQ;'
						'trusted_connection=yes;')

cursor = cnxn.cursor()

cursor.execute("select top 10 SOURCECODE from Selections")

row = cursor.fetchall()
if row:
	print(row)

