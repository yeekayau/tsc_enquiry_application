import datetime

from flask.ext.login import UserMixin
from peewee import *
from enquiry_database import EnquiryDatabase

DATABASE = EnquiryDatabase()

class Enquiry(Model):
	enquiry_id = IntegerField()
	result_status = CharField()
	date_start = DateTimeField()
	date_finish = DateTimeField()
	user_browser = CharField()
	user_os = CharField()
	user_referrer = CharField()
	completed_by = CharField()
	client_pguid = CharField()
	firstname = CharField()
	lastname = CharField()
	dateofbirth = DateTimeField()
	caregiver_firstname = CharField()
	caregiver_lastname = CharField()
	relationship_to_child = CharField()
	suburb = CharField()
	postcode = IntegerField()
	caregiver_phone = IntegerField()

	class Meta():
		database = DATABASE
		order_by = ('date_finish',)