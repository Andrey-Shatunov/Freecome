from bson.objectid import ObjectId
import json

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

def entity_to_str(entity):
    str1=""
    for i,value in enumerate(entity,1):
        str1=str1+str(JSONEncoder().encode(value))+''', '''

    str1=str1[0:(len(str1)-2)]
    str1='''['''+str1+''']'''
    return str1
    
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False