from mongoengine.fields import BooleanField
from mongoengine import *
from Read_Mongo import*

# class 223PB1595(Document):
#      ctrlID = IntField()
#      lotNo = StringField()
#      rec_datatime = StringField(max_length=26)
#      unit_data = ListField()

class app_settings(Document):
    SAVED = ListField()
    logs_showing = BooleanField()
    rec_datetime = StringField(max_length=26)
    
class lot_no(Document):

    ctrlID = IntField(max_value=1000)
    lotNo = StringField(max_length=10)
    
    rec_datetime = StringField(max_length=26)
    unit_data = ListField()

