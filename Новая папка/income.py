import json
#import bottle
from bottle import route, run, request, abort
from pymongo import Connection
from bson.json_util import dumps

def entity_to_str(entity):
    str1=""
    for i,value in enumerate(entity,1):
        print(str(value)[5])
        #str1=str1+"123"+str(value)
        str1=str1+"\'"+str(i)+"\'"+''': '''+str(value)+''', '''
    #print(json.dumps(entity))
    
    #str1='''{'''+str1
      
    
    str1=str1[0:(len(str1)-2)]
    str1='''{'''+str1+'''}'''
	return str1