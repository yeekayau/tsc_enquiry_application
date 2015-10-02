
# Family Survey

import urllib.request
from xml.etree import ElementTree

fs_familysurvey_api_key = 'Uypjm786XfmF'
fs_familysurvey_apibase_url = 'https://fs30.formsite.com/api/users/TheShepherdCentre/forms/form2/'

# Opens the Url - A 'POST' request, post the api_key to ask for data
x = urllib.request.urlopen(fs_familysurvey_apibase_url + 'results?fs_api_key='
							+ fs_familysurvey_api_key)

# parses the URL data as an XML element tree
tree = ElementTree.parse(x)

# The root element would be the top tag - in our case, this would be the fs_response tag
fs_response = tree.getroot()

# This is the 2nd level tag, so it's only <results> and <total_results> tags which are
# on the same level
for child in fs_response:
	print (child.tag, child.attrib)

#iter_ = tree.getiterator()
#for elem in iter_:
#    print (elem.tag)

top_level = fs_response.getchildren()

for next_level in top_level:
    results = next_level.getchildren()
    
    # No result.text is printed as the element itself (which is each result) does not have
    # an atribute
    for result in results:
        print (result.tag, result.attrib)
        # next level of tags in each result, includes <metas> and <items tags>,
        # No text is printed as the tag itself does not have a value

        for metas_items in result:

            for meta in metas_items:

                print (meta.tag, meta.attrib, meta.text)

                for row in meta:
                    print(row.tag, row.attrib, row.text)
                    for value in row:
                        print(value.tag, value.attrib, value.text)
# print(x.read())