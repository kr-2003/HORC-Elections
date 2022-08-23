from logging import exception
from turtle import pos
import pandas as pd
import csv
import re

def create_import_data():
    data = {'hostel':[],'post_name':[],'candidates':[]}
    import_data = pd.DataFrame(data)

    candidates = dict()

    with open('Data_Clean/Cleaned_Posts_List.csv') as file_obj:

        reader_obj = csv.DictReader(file_obj)
        for row in reader_obj:
            try:
                name , email , hostel , post_name = row['Name'] , row['Email'] , row['Hostel'] , row['Post_Name']
                print(name , email,hostel,post_name)

                k = tuple([hostel,post_name])

                x = list(candidates.get(k,()))
                x.append(email)
                print(x)
                v = tuple(x)

                # print(type(k),type(v))

                candidates[k] = v
                
            except Exception as e:
                print("Exception ",e)
                pass

    for k,v in candidates.items():
        details = {'hostel': k[0] ,'post_name': k[1] ,'candidates': ",".join(list(v))}
        import_data = import_data.append(details, ignore_index = True)

    import_data.to_csv('Data_Import/posts_import.csv',index = False)