

from xml.etree import ElementTree

def getPreferredContactDayTime(day, enquiry_dict):
    if day.attrib.get('index') == '0':
        d = 'mon'
    elif day.attrib.get('index') == '1':
        d = 'tues'
    elif day.attrib.get('index') == '2':
        d = 'wed'
    elif day.attrib.get('index') == '3':
        d = 'thurs'
    elif day.attrib.get('index') == '4':
        d = 'fri'

    for time in day:
        if time.attrib.get('index') == '0':
            enquiry_dict['p_c_day_' + d + '_morning'] = time.text        
        if time.attrib.get('index') == '1':
            enquiry_dict['p_c_day_' + d + '_lunch'] = time.text
        if time.attrib.get('index') == '2':
            enquiry_dict['p_c_day_' + d + '_afternoon'] = time.text


def getAppFormData(tree):
    enquiry_list = []
# Node is every element cascading down
    for node in tree.iter():
    
        if node.attrib.get('index') == '0':
            enquiry_dict = {}
            for child in node:
                print('Firstname: ' + child.text)

                enquiry_dict['Firstname'] = child.text


        if node.attrib.get('index') == '1':
            for child in node:
                print('Lastname: ' + child.text)

                enquiry_dict['Lastname'] = child.text
    
            enquiry_list.append(enquiry_dict)
            enquiry_dict = None

    return enquiry_list


def getEnquiryFormData(tree):
    enquiry_list = []

    for node in tree.iter():
    
        if node.attrib.get('id') == 'result_status':
            enquiry_dict = {}

            enquiry_dict['result_status'] = node.text

        if node.attrib.get('id') == 'date_start':
            enquiry_dict['date_start'] = node.text

        if node.attrib.get('id') == 'date_finish':
            enquiry_dict['date_finish'] = node.text

        if node.attrib.get('id') == 'user_browser':
            enquiry_dict['user_browser'] = node.text

        if node.attrib.get('id') == 'user_os':
            enquiry_dict['user_os'] = node.text

        if node.attrib.get('id') == 'user_referrer':
            enquiry_dict['user_referrer'] = node.text

        if node.attrib.get('id') == '172':
            for node in node:
                enquiry_dict['Firstname'] = node.text

        if node.attrib.get('id') == '173':
            for child in node:
                enquiry_dict['lastname'] = child.text
    
        if node.attrib.get('id') == '48':
            for child in node:
                enquiry_dict['dateofbirth'] = child.text

        if node.attrib.get('id') == '46':
            for child in node:
                enquiry_dict['caregiver_firstname'] = child.text        
            
        if node.attrib.get('id') == '47':
            for child in node:
                enquiry_dict['caregiver_lastname'] = child.text    
            
        if node.attrib.get('id') == '181':
            for child in node:
                enquiry_dict['relationship_to_child'] = child.text    

        if node.attrib.get('id') == '175':
            for child in node:
                enquiry_dict['suburb'] = child.text

        if node.attrib.get('id') == '177':
            for child in node:
                enquiry_dict['caregiver_phone'] = child.text        

        if node.attrib.get('id') == '186':
            for child in node:
                enquiry_dict['caregiver_alt_phone'] = child.text

        if node.attrib.get('id') == '182':
            for child in node:
                enquiry_dict['caregiver_email'] = child.text

        if node.attrib.get('id') == '176':
            for child in node:
                enquiry_dict['preferred_contact_method'] = child.text

        if node.attrib.get('id') == '184':
            for day in node:
                getPreferredContactDayTime(day, enquiry_dict)

            enquiry_list.append(enquiry_dict)
            enquiry_dict = None

    return enquiry_list

    