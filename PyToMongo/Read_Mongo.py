#from config import *
from mongoengine import *
import pandas as pd
from class_mongo import *

class main(object):

     def __init__(self):
        
         self.connect_mongoDB()

     def connect_mongoDB(self):

        print("\n----- Connect MongoDB -----")
        connect(db='SPC_DB_1090',host='mongodb://mtl90526:mte40@191.191.5.35:27017/admin?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
        print("Connected to MongoDB")

     def query_doc(lot_no,col_name):
         new_group = lot_no.switch_collection(col_name)
         new_objects = QuerySet(lot_no, new_group._get_collection())   
         
         data = []
         for i in new_objects:
             data2 = {}

             data2["datetime"] = i.rec_datetime
             data2["ctrlID"] = i.ctrlID
             data2["coreID"] = i.coreID
             data2["lotNo"] = i.lotNo
             data2["judgement"] = i.judgement
             for j in i.unit_data:
                 data2.update({j["param_name"]: j["cur_value"]})
             print(data2)
             data.append(data2)

         df = pd.DataFrame(data)
         print("df=\n", df)
         return df

     lot_list = ["223PB1595", "223PB1596"]
     df_list = []
     for j in lot_list:
        df_list.append(query_doc(lot_no(), j))
     vertical_concat = pd.concat(df_list, axis=0)
     # print("vertical_concat=", vertical_concat)
     # export to file
     vertical_concat.to_excel(f"./data/all_data.xlsx", index=False, header=True)
    
main()
