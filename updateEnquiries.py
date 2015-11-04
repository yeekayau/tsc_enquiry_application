

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
 
def validatePreferredContactDayTime(contact_time):
    if result.get(contact_time):
        c_time = 1
    else:
        c_time = 0
    return c_time

def checkRecordinDB(cnxn, result):
    date_start = result.get('date_start')
    date_finish = result.get('date_finish') 
    Lastname = result.get('Lastname')
    Firstname = result.get('Firstname')

    if result.get('postcode'): 
        postcode = result.get('postcode')
    else:
        postcode = 0

    dateofbirth = result.get('dateofbirth')

    cursor = cnxn.cursor()
    cursor.execute("""select date_start, date_finish, firstname, lastname,
                             postcode, dateofbirth
                      from Enquiries
                      where date_start = ? and date_finish = ?
                      and lastname = ? and firstname = ? and postcode = ?
                      and dateofbirth = ?
                   """, 
                   (date_start, date_finish, Lastname, Firstname, postcode, dateofbirth)
                   )
    rows = cursor.fetchall()
    if rows:
        already_in_db = 1
    else:
        already_in_db = 0

    return already_in_db

# ----------------------------------------
# Create connection to DB
cnxn = pypyodbc.connect('Driver={SQL Server Native Client 10.0};'
						'server=DASDB01;'
						'database=IA_CDIS;'
						'trusted_connection=yes;')

#cursor = cnxn.cursor()
# 38 items

sql = ('insert into Enquiries('
'result_status, '
'date_start, '
'date_finish, '
'user_browser, '
'user_os, '
'user_referrer, '
'completed_by, '
'client_pguid, '
'firstname, '
'lastname, '
'dateofbirth, '
'caregiver_firstname, ' 
'caregiver_lastname, '
'relationship_to_child, '
'suburb, '
'postcode, '
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
'not_joined_reason) ' #38
'values '
'(?,?,?,?,?,?,?,Newid(),?,?,?,?,?,?,?,?,?,?,?,?,?,'
'?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,0,0)')


for result in enquiry_list:
    
    # method to check whether this enquiry record is already in the database
    already_in_db = checkRecordinDB(cnxn, result)

    if already_in_db == 0:

        cursor = cnxn.cursor()

        if result.get('result_status'):
            result_status = result.get('result_status') 
        else:
            result_status = 'Incomplete'

        date_start = result.get('date_start')
        date_finish = result.get('date_finish') 
        user_browser = result.get('user_browser')
        user_os = result.get('user_os') 
        user_referrer = result.get('user_referrer')

        if result.get('completed_by'):
            completed_by = result.get('completed_by') 
        else:
            completed_by = 'old result'

        Lastname = result.get('Lastname').strip()
        Firstname = result.get('Firstname').strip()
        dateofbirth = result.get('dateofbirth')
        caregiver_firstname = result.get('caregiver_firstname').strip()
        caregiver_lastname = result.get('caregiver_lastname').strip()
        relationship_to_child = result.get('relationship_to_child')
        suburb = result.get('suburb').strip()

        if result.get('postcode'): 
            postcode = result.get('postcode')
        else:
            postcode = 0

        caregiver_phone = result.get('caregiver_phone')
        caregiver_alt_phone = result.get('caregiver_alt_phone')
        
        if result.get('caregiver_email'):
            caregiver_email = result.get('caregiver_email').strip()
        else:
            caregiver_email = result.get('caregiver_email')

        preferred_contact_method = result.get('preferred_contact_method')
        p_c_day_mon_morning = validatePreferredContactDayTime('p_c_day_mon_morning')
        p_c_day_mon_lunch = validatePreferredContactDayTime('p_c_day_mon_lunch')
        p_c_day_mon_afternoon = validatePreferredContactDayTime('p_c_day_mon_afternoon')    
        p_c_day_tues_morning = validatePreferredContactDayTime('p_c_day_tues_morning')
        p_c_day_tues_lunch = validatePreferredContactDayTime('p_c_day_tues_lunch')
        p_c_day_tues_afternoon = validatePreferredContactDayTime('p_c_day_tues_afternoon')
        p_c_day_wed_morning = validatePreferredContactDayTime('p_c_day_wed_morning')
        p_c_day_wed_lunch = validatePreferredContactDayTime('p_c_day_wed_lunch')
        p_c_day_wed_afternoon = validatePreferredContactDayTime('p_c_day_wed_afternoon')
        p_c_day_thurs_morning = validatePreferredContactDayTime('p_c_day_thurs_morning')
        p_c_day_thurs_lunch = validatePreferredContactDayTime('p_c_day_thurs_lunch')
        p_c_day_thurs_afternoon = validatePreferredContactDayTime('p_c_day_thurs_afternoon')
        p_c_day_fri_morning = validatePreferredContactDayTime('p_c_day_fri_morning')
        p_c_day_fri_lunch = validatePreferredContactDayTime('p_c_day_fri_lunch')
        p_c_day_fri_afternoon = validatePreferredContactDayTime('p_c_day_fri_afternoon')

        if result.get('How_can_we_help'):
            how_can_we_help = result.get('How_can_we_help')
        else:
            how_can_we_help = 'This is a mystery'

        insert_tuple = (result_status, 
                    date_start, 
                    date_finish,
                    user_browser, 
                    user_os, 
                    user_referrer, 
                    completed_by,
                    Firstname, 
                    Lastname, 
                    dateofbirth,
                    caregiver_firstname, 
                    caregiver_lastname, 
                    relationship_to_child, 
                    suburb, 
                    postcode,
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

        cursor.execute(sql, insert_tuple)
        cnxn.commit()
