import pandas as pd
import csv
import re
import os
from string import capwords


def valid(name,email,hostel,post,POST_NAMES,HOSTEL_NAMES):
    if (name is None) or (email is None) or (hostel is None) or (post is None):
        return False
    
    if (name == "") or (email == "") or (hostel == "") or (post == ""):
        return False

    if post not in POST_NAMES:
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


def clean_candidates(FILE_NAME,POST_NAMES,HOSTEL_NAMES):

    data = {'Name':[],'Email':[],'Hostel':[],'Post_Name':[]}
    cleaned_data = pd.DataFrame(data)

    with open(os.path.join('Data_Raw',FILE_NAME)) as file_obj:

        reader_obj = csv.DictReader(file_obj)
        for row in reader_obj:
            try:
                name , email , hostel , post = row['Name'] , row['Email Address'] , row['Hostel']  , row['HORC post you are applying for']

                if valid(name,email,hostel,post,POST_NAMES,HOSTEL_NAMES):
                    details = {'Name': capwords(name.lower().capitalize())  , 'Email': email , 'Hostel' : hostel , 'Post_Name' : post }
                    cleaned_data = cleaned_data.append(details, ignore_index = True)

            except Exception as e:
                print(e)
                pass

    for post_name in POST_NAMES:
        for hostel in HOSTEL_NAMES:
            details = {'Name': "NOTA"  , 'Email': f"nota_{hostel}@iiti.ac.in" , 'Hostel' : hostel , 'Post_Name' : post_name }
            cleaned_data = cleaned_data.append(details, ignore_index = True)



    cleaned_data.to_csv('Data_Clean/Cleaned_Posts_List.csv',index = False)

 

