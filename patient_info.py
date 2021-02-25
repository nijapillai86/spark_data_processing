from disease_keywords_update import conditions, key_names
from bs4 import BeautifulSoup
from utils import validate_age
#from pyspark.sql import Row
import re
import json

def get_personal_details(encounter):
    
    '''
    patient_info = {'id' : demographics['patient_id'],
        "name" : demographics['name']['given']+' '+demographics['name']['family'],
		"date_of_birth" : demographics['dob'],
		"age" : int(demographics['age']),
        "file_name" : demographics['file_name']
	}
    print([Row(v) for k,v in patient_info.items()])
    '''
    demographics = encounter['demographics']['parser']
    file_name = ""
    age = 0
    if validate_age(demographics['age']):
        age = int(validate_age(demographics['age']))
    if 'file_name' in demographics:
        file_name = demographics['file_name']

    patient_data = [(demographics['patient_id'],
        demographics['name']['given'],
        demographics['name']['family'],
		demographics['dob'],
		age,
        file_name ,
        json.dumps(encounter)
    )]
    #print(json.dumps(patient_info))
    return patient_data


def extract_text(section):
    """This method extracts plain text form json files :param section: json
    object :return: plain text

    Args:
        section:
    """
    text = json.dumps(section)
    soup = BeautifulSoup(text, "html.parser")  # Remove HTML tags from JSON
    text = soup.get_text().lower()
    text = re.sub(r'\n+', '. ', text)
    text = re.sub(r'[\]u[0-9]{5}', '. ', text)
    text = re.sub(r'\d{2}/\d{2}/\d{4}', ' ', text)
    for item in ['"','-','{','}','[',']',',','(',')',":",'\\']:
        text = text.replace(item,' ')


    text = re.sub('\s\s+', ' ', text)  # Remove extra spaces
    # text = str(TextBlob(text).correct())
    return text
 
def get_sections(ccd_json,NON_SECTIONS):
    sectionElements = []
    for s in list(ccd_json):
        if s not in NON_SECTIONS:
            if isinstance(ccd_json[s], dict):
                sectionElements.append(s)
            else:
                continue
    return  sectionElements  
       
def check_condition_keys(key_set, patient_json):

    NON_SECTIONS = ['demographics','document','family_history', 'social_history','icd_codes','vitals']
    sectionElements = get_sections(patient_json,NON_SECTIONS)
    inclusion = []
    icd_code_exist = []
    mainConditions = []
    for section in sectionElements:
        sec = extract_text(patient_json[section]['parser'])
        if section != "medications":
            icd_code_exist += re.findall('|'.join(conditions[key_set]['icd_codes']), sec, re.IGNORECASE)
            keywords = re.findall('|'.join(conditions[key_set]['main']), sec, re.IGNORECASE) 
            mainConditions += keywords#list(keys_main.keys())
        else:
            
            mainConditions += re.findall('|'.join(conditions[key_set]['main']), sec, re.IGNORECASE)

    inclusion.append(icd_code_exist)
    inclusion.append(mainConditions)
    return inclusion
    	
def get_condition(encounter):
    encounter = json.loads(encounter)
    pid  = encounter['demographics']['parser']['patient_id']
    patient_disease =  'None'
    disease_keyword_list = {}
    disease_name_list = []
    disease_key = list(key_names.values())
    for key in disease_key:
        keywords_list = []
        inclusion = check_condition_keys(key, encounter)
        inclusion = inclusion[0] + inclusion[1]
        if inclusion:
            keywords_list += inclusion
        disease_keyword_list[key] = list(filter(None, keywords_list))
        #total_keywords += len(disease_keyword_list[key])
        disease_name_list.append(disease_keyword_list[key])
    disease_name_list.sort(key = lambda x: len(x)) 
    #print(disease_name_list)
    if len(disease_name_list[-1]) == 0:
        #print('No disease found for ', pid)
        patient_disease = 'None'

    else:
        condition_keys = []
        for disease_key, arr in disease_keyword_list.items():  
            if arr != []:
                condition_keys.append(disease_key)
        patient_disease = ','.join(condition_keys)
    #print(f'{patient_disease.strip()} found for {pid}')
    return patient_disease.strip()