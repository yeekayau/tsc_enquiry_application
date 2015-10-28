

from xml.etree import ElementTree


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
            print('result_status: ' + node.text)

            enquiry_dict['result_status'] = node.text

        if node.attrib.get('id') == 'date_start':
            print('date_start: ' + node.text)

            enquiry_dict['date_start'] = node.text

        if node.attrib.get('id') == 'date_finish':
            print('date_finish: ' + node.text)

            enquiry_dict['date_finish'] = node.text

        if node.attrib.get('id') == 'user_browser':
            print('user_browser: ' + node.text)

            enquiry_dict['user_browser'] = node.text

        if node.attrib.get('id') == 'user_os':
            print('user_os: ' + node.text)

            enquiry_dict['user_os'] = node.text

        if node.attrib.get('id') == 'user_referrer':
            print('user_referrer: ' + node.text)

            enquiry_dict['user_referrer'] = node.text

        if node.attrib.get('id') == '172':
            for node in node:
                print('Firstname: ' + node.text)

                enquiry_dict['Firstname'] = node.text

        if node.attrib.get('id') == '173':
            for child in node:
                print('Lastname: ' + child.text)

                enquiry_dict['lastname'] = child.text
    
        if node.attrib.get('id') == '48':
            for child in node:
                print('dateofbirth: ' + child.text)

                enquiry_dict['dateofbirth'] = child.text

        if node.attrib.get('id') == '46':
            for child in node:
                print('caregiver_firstname: ' + child.text)

                enquiry_dict['caregiver_firstname'] = child.text        
            
        if node.attrib.get('id') == '47':
            for child in node:
                print('caregiver_lastname: ' + child.text)

                enquiry_dict['caregiver_lastname'] = child.text    
            
        if node.attrib.get('id') == '181':
            for child in node:
                print('relationship_to_child: ' + child.text)

                enquiry_dict['relationship_to_child'] = child.text    

        if node.attrib.get('id') == '175':
            for child in node:
                print('suburb: ' + child.text)

                enquiry_dict['suburb'] = child.text

        if node.attrib.get('id') == '177':
            for child in node:
                print('caregiver_phone: ' + child.text)

                enquiry_dict['caregiver_phone'] = child.text        

        if node.attrib.get('id') == '186':
            for child in node:
                print('caregiver_alt_phone: ' + child.text)

                enquiry_dict['caregiver_alt_phone'] = child.text

        if node.attrib.get('id') == '182':
            for child in node:
                print('caregiver_email: ' + child.text)

                enquiry_dict['caregiver_email'] = child.text

        if node.attrib.get('id') == '176':
            for child in node:
                print('preferred_contact_method: ' + child.text)

                enquiry_dict['preferred_contact_method'] = child.text

        if node.attrib.get('id') == '184':
            for day in node:
                if day.attrib.get('index') == '0':
                    for time in day:
                        if time.attrib.get('index') == '0':
                            print('p_c_day_mon_morning: ' + time.text)
                            enquiry_dict['p_c_day_mon_morning'] = time.text        
                        if time.attrib.get('index') == '1':
                            print('p_c_day_mon_lunch: ' + time.text)
                            enquiry_dict['p_c_day_mon_lunch'] = time.text
                        if time.attrib.get('index') == '2':
                            print('p_c_day_mon_afternoon: ' + time.text)
                            enquiry_dict['p_c_day_mon_afternoon'] = time.text

                if day.attrib.get('index') == '1':
                    for time in day:
                        if time.attrib.get('index') == '0':
                            print('p_c_day_tues_morning: ' + time.text)
                            enquiry_dict['p_c_day_tues_morning'] = time.text        
                        if time.attrib.get('index') == '1':
                            print('p_c_day_tues_lunch: ' + time.text)
                            enquiry_dict['p_c_day_tues_lunch'] = time.text
                        if time.attrib.get('index') == '2':
                            print('p_c_day_tues_afternoon: ' + time.text)
                            enquiry_dict['p_c_day_tues_afternoon'] = time.text

            enquiry_list.append(enquiry_dict)
            enquiry_dict = None

    return enquiry_list

    