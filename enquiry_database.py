from peewee import Database
import pypyodbc

class EnquiryDatabase(Database):
	def _connect(self):
		return cnxn = pypyodbc.connect('Driver={SQL Server Native Client 10.0};'
										'server=DASDB01;'
										'database=IA_CDIS;'
										'trusted_connection=yes;'
										'MARS_Connection=yes;')
