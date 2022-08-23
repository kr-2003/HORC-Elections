import pandas as pd
import csv
import re
import os
from string import capwords

def valid(name,email,hostel,HOSTEL_NAMES):
    if (name is None) or (email is None) or (hostel is None):
        return False
    
    if (name == "") or (email == "") or (hostel == ""):
        return False

    if hostel not in HOSTEL_NAMES:
        return False

    if email.endswith("@iiti.ac.in")==False:
        return False

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if(re.fullmatch(regex, email)):
        return True
    else:
        return False
 
def clean_residents(FILE_NAME,HOSTEL_NAMES):
    data = {'Name':[],'Email':[],'Hostel':[]}
    cleaned_data = pd.DataFrame(data)

    with open(os.path.join('Data_Raw',FILE_NAME)) as file_obj:

        reader_obj = csv.DictReader(file_obj)
        for row in reader_obj:
            try:
                name , email , hostel = row['Name'] , row['Email'] , row['HOSTEL']

                if valid(name,email,hostel,HOSTEL_NAMES):
                    details = {'Name': capwords(name.lower().capitalize())  , 'Email': email , 'Hostel' : hostel }
                    cleaned_data = cleaned_data.append(details, ignore_index = True)
            except:
                pass

    cleaned_data.to_csv('Data_Clean/Cleaned_Residence_List.csv',index = False)