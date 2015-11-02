

from formXMLDataHandler import getEnquiryFormData
import pypyodbc
import urllib.request
from xml.etree import ElementTree

fs_api_key = 'Uypjm786XfmF'
fs_apibase_url = 'https://fs30.formsite.com/api/users/TheShepherdCentre/forms/NewEnquiry/'

# Opens the Url - A 'POST' request, post the api_key to ask for data
x = urllib.request.urlopen(fs_apibase_url + 'results?fs_api_key='
							+ fs_api_key)

# parses the URL data as an XML element tree
tree = ElementTree.parse(x)

enquiry_list = getEnquiryFormData(tree)

# Lets just see what we got
for dictionary in enquiry_list:
    print('********************************************************************')
    for key, name in dictionary.items():
        print(key + ': ' + name)
 
# ----------------------------------------
# Create connection to DB
cnxn = pypyodbc.connect('Driver={SQL Server Native Client 10.0};'
						'server=DASDB01;'
						'database=IA_CDIS;'
						'trusted_connection=yes;')

cursor = cnxn.cursor()
# 37 items
sql = ('insert into Enquires('
'result_status, '
'date_start, '
'date_finish, '
'user_browser, '
'user_os, '
'user_referrer, '
'client_p_guid, '
'Lastname, '
'Firstname, '
'lastname, '
'dateofbirth, '
'caregiver_firstname, ' 
'caregiver_lastname, '
'relationship_to_child, '
'suburb, '
'caregiver_phone, '
'caregiver_alt_phone, '
'caregiver_email, '
'preferred_contact_method, '
'[p_c_day_mon_morning], '
'[p_c_day_mon_lunch], '
'[p_c_day_mon_afternoon], '
'[p_c_day_tues_morning], '
'[p_c_day_tues_lunch], '
'[p_c_day_tues_afternoon], '
'[p_c_day_wed_morning], '
'[p_c_day_wed_lunch], '
'[p_c_day_wed_afternoon], '
'[p_c_day_thurs_morning], '
'[p_c_day_thurs_lunch], '
'[p_c_day_thurs_afternoon], '
'[p_c_day_fri_morning], '
'[p_c_day_fri_lunch], '
'[p_c_day_fri_afternoon], '
'[how_can_we_help], '
'joined_program,'
'not_joined_reason'
'values '
'({},{},{},{},{},{},Newid(),{},{},{},{},{},{},{},{},{},{},{},{},'
'{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},0,NULL)')

for result in enquiry_list:
    
    if result.get('result_status'):
        result_status = "'{}'".format(result.get('result_status')) 
    else:
        result_status = 'Incomplete'

    date_start = "'{}'".format(result.get('date_start'))
    date_finish = "'{}'".format(result.get('date_finish')) 
    user_browser = "'{}'".format(result.get('user_browser'))
    user_os = "'{}'".format(result.get('user_os')) 
    user_referrer = "'{}'".format(result.get('user_referrer'))
    Lastname = "'{}'".format(result.get('Lastname'))
    Firstname = "'{}'".format(result.get('Firstname'))
    dateofbirth = "'{}'".format(result.get('dateofbirth'))
    caregiver_firstname = "'{}'".format(result.get('caregiver_firstname'))
    caregiver_lastname = "'{}'".format(result.get('caregiver_lastname'))
    relationship_to_child = "'{}'".format(result.get('relationship_to_child'))
    suburb = "'{}'".format(result.get('suburb'))
    caregiver_phone = "'{}'".format(result.get('caregiver_phone'))
    caregiver_alt_phone = "'{}'".format(result.get('caregiver_alt_phone'))
    caregiver_email = "'{}'".format(result.get('caregiver_email'))
    preferred_contact_method = "'{}'".format(result.get('preferred_contact_method'))

    if result.get('p_c_day_mon_morning'):
        p_c_day_mon_morning = "'{}'".format(result.get('p_c_day_mon_morning'))
    else:
        p_c_day_mon_morning = 0
        
    p_c_day_mon_lunch = "'{}'".format(result.get('p_c_day_mon_lunch'))
    p_c_day_mon_afternoon = "'{}'".format(result.get('p_c_day_mon_afternoon'))
    p_c_day_tues_morning = "'{}'".format(result.get('p_c_day_tues_morning'))
    p_c_day_tues_lunch = "'{}'".format(result.get('p_c_day_tues_lunch'))
    p_c_day_tues_afternoon = "'{}'".format(result.get('p_c_day_tues_afternoon'))
    p_c_day_wed_morning = "'{}'".format(result.get('p_c_day_wed_morning'))
    p_c_day_wed_lunch = "'{}'".format(result.get('p_c_day_wed_lunch'))
    p_c_day_wed_afternoon = "'{}'".format(result.get('p_c_day_wed_afternoon'))
    p_c_day_thurs_morning = "'{}'".format(result.get('p_c_day_thurs_morning'))
    p_c_day_thurs_lunch = "'{}'".format(result.get('p_c_day_thurs_lunch'))
    p_c_day_thurs_afternoon = "'{}'".format(result.get('p_c_day_thurs_afternoon'))
    p_c_day_fri_morning = "'{}'".format(result.get('p_c_day_fri_morning'))
    p_c_day_fri_lunch = "'{}'".format(result.get('p_c_day_fri_lunch'))
    p_c_day_fri_afternoon = "'{}'".format(result.get('p_c_day_fri_afternoon'))
    how_can_we_help = "'{}'".format(result.get('how_can_we_help'))

    insert = sql.format(result_status, 
                        date_start, 
                        date_finish,
                        user_browser, 
                        user_os, 
                        user_referrer, 
                        Firstname, 
                        Lastname, 
                        dateofbirth, 
                        caregiver_firstname, 
                        caregiver_lastname, 
                        relationship_to_child, 
                        suburb, 
                        caregiver_phone, 
                        caregiver_alt_phone, 
                        caregiver_email, 
                        preferred_contact_method,
                        p_c_day_mon_morning,
                        p_c_day_mon_lunch,
                        p_c_day_mon_afternoon,
                        p_c_day_tues_morning,
                        p_c_day_tues_lunch,
                        p_c_day_tues_afternoon,
                        p_c_day_wed_morning,
                        p_c_day_wed_lunch,
                        p_c_day_wed_afternoon,
                        p_c_day_thurs_morning,
                        p_c_day_thurs_lunch,
                        p_c_day_thurs_afternoon, 
                        p_c_day_fri_morning, 
                        p_c_day_fri_lunch, 
                        p_c_day_fri_afternoon, 
                        how_can_we_help)
    print(insert)
#     cursor.execute(insert)
#     cnxn.commit()



