import pypyodbc

cnxn = pypyodbc.connect('Driver={SQL Server Native Client 10.0};'
						'server=DASDB01;'
						'database=IA_CDIS;'
						'trusted_connection=yes;')

cursor = cnxn.cursor()

cursor.execute("select top 10 ApplicationUser from WindowsUsers")

row = cursor.fetchall()
if row:
	print(row)

cursor.execute("insert into Form_test(p_guid, Lastname, Firstname) values (Newid(), 'Yau', 'Yeeka')")
cnxn.commit()


