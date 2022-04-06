from pymongo import MongoClient
import pandas as pd
# client = MongoClient('localhost',27017)
client = MongoClient(host='mongodb://mtl90526:mte40@191.191.5.35:27017/admin?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')


db = client.SPC_DB_1090
tb = db['app_settings']
result = tb.find()
print(result)

for i in result:
    print(i)

df = pd.DataFrame(result)
# df.head
print(df)