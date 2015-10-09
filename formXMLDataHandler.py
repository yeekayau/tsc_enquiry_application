

from xml.etree import ElementTree


def getAppFormData(tree):
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

    return person_list