

# AppForm Test

import urllib.request
from xml.etree import ElementTree

fs_api_key = 'Uypjm786XfmF'
fs_apibase_url = 'https://fs30.formsite.com/api/users/TheShepherdCentre/forms/form17/'

# Opens the Url - A 'POST' request, post the api_key to ask for data
x = urllib.request.urlopen(fs_apibase_url + 'results?fs_api_key='
							+ fs_api_key)

# parses the URL data as an XML element tree
tree = ElementTree.parse(x)

person_list = []

# Node is every element cascading down
for node in tree.iter():
    
    if node.attrib.get('index') == '0':
        person_dict = {}
        for child in node:
            print('Firstname: ' + child.text)

            person_dict['Firstname'] = child.text


    if node.attrib.get('index') == '1':
        for child in node:
            print('Lastname: ' + child.text)

            person_dict['Lastname'] = child.text
    
        person_list.append(person_dict)
        person_dict = None

print(person_list)
#for item in person_list:
#    print(person_dict)
