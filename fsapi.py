
# Family Survey

import urllib.request
from xml.etree import ElementTree

fs_familysurvey_api_key = 'Uypjm786XfmF'
fs_familysurvey_apibase_url = 'https://fs30.formsite.com/api/users/TheShepherdCentre/forms/form2/'

# Opens the Url - A 'POST' request, post the api_key to ask for data
x = urllib.request.urlopen(fs_familysurvey_apibase_url + 'results?fs_api_key='
							+ fs_familysurvey_api_key)

tree = ElementTree.parse(x)

# The root element would be the top tag - in our case, this would be the fs_response tag
root = tree.getroot()

for child in root:
	print (child.tag, child.attrib)


# print(x.read())