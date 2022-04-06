from mongoengine import connect


class Settings(object):
    # MONGODB = {
    #     'username':"mtl91475",
    #     'password':"mt920",
    #     'hostname':"localhost",
    #     'dbname':"SPC_DB_1090_2",
    #     'port':27017,
    #     'uname_root': "mtl91430",
    #     'pass_root': "mt730"

    # }

    connect(db='SPC_DB_1090',host='mongodb://mtl90526:mte40@191.191.5.35:27017/admin?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')

