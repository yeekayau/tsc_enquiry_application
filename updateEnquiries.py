

# AppForm Test
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

for dictionary in enquiry_list:
    print('********************************************************************')
    for key, name in dictionary.items():
        print(key + ': ' + name)
 
# ----------------------------------------
# Create connection to DB
# cnxn = pypyodbc.connect('Driver={SQL Server Native Client 10.0};'
# 						'server=DASDB01;'
# 						'database=IA_CDIS;'
# 						'trusted_connection=yes;')

# cursor = cnxn.cursor()

# sql = 'insert into Form_test(p_guid, Lastname, Firstname) values (Newid(),{},{})'

# for result in person_list:
#     Lastname = "'{}'".format(result.get('Lastname'))
#     Firstname = "'{}'".format(result.get('Firstname'))
#     insert = sql.format(Lastname, Firstname)
#     print(insert)
#     cursor.execute(insert)
#     cnxn.commit()



