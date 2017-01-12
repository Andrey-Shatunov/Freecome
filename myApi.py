import json
import bson
#import bottle
from bottle import route, run, request, abort
from pymongo import Connection
import pymongo
#from bson.json_util import dumps
from income_to import entity_to_str
from bson.objectid import ObjectId

connection = Connection('localhost', 27017)
db = connection.mydatabase

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
###
#entity = db['documents'].find_one({'_id':'doc1'})
#print(entity)

#********************************************PUT************************************************* 
@route('/income', method='PUT')
def put_document():
    data = request.body.readline().decode('utf8')
    lwist1=['id_user','sum','category','note','data']
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    if '_id' not in entity:
        abort(400, 'No _id specified')
        
    list_key=list(entity.keys())
    
    if len(list_key) > 2:
        abort(400, 'Many parametr')
        
    
    
    print("list_key"+str(list_key))
    print(lwist1.count(list_key[0]))
    
    list_key.remove('_id')
    print("list_key"+str(list_key))
    if lwist1.count(list_key[0]) == 0:
        abort(400, 'Wrong parametr')
    try:
        print(entity.keys())
        result=db['income'].update({"_id": ObjectId(entity['_id'])}, {"$set":{list_key[0]: entity[list_key[0]]}})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    return result
#********************************************POST*************************************************        
@route('/income', method='POST')
def post_document():
    data = request.body.readline().decode('utf8')
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    print(entity)
    if '_id' in entity:
        abort(400, 'Id generate auto')
 #   if '_id_user' not in entity:
  #      abort(400, 'No _id_user specified')
    try:
        db['income'].save(entity)
    except pymongo.errors.WriteError as ve:
        abort(400, str(ve))
#********************************************GET*************************************************       
@route('/income', method='GET')
def get_all_income():
    entity = db['income'].find()
    if not entity:
        abort(404, 'DB is empty')
    #print(json.loads("{\"1\":\"2\"}"))
    return json.loads(entity_to_str(entity))

#get income for _id_user   
@route('/income/:id', method='GET')
def get_income(id):
    print(id)
    entity = db['income'].find_one({'_id': ObjectId(id)})
    print(entity)
    if not entity:
        abort(404, 'No document with id %s' % id)
    return JSONEncoder().encode(entity)

#get user for id
@route('/income/user/:id', method='GET')
def get_income_for_user(id):
    entity = db['income'].find_one({'_id_user':id})
    print(entity)
    if not entity:
        abort(404, 'No document with id %s' % id)
    return entity
#********************************************DELETE*************************************************    
@route('/income/:id', method='DELETE')
def delete_income(id):
    entity = db['income'].remove({'_id':id})
    #if not entity:
        #abort(404, 'No document with id %s' % id)
    #result = db['income'].remove({'_id_user':id})
    return entity
 
@route('/income/all/', method='DELETE')
def delete_income_all():
    try:
        entity = db['income'].remove({})
    except:
        print ('error/exception')
    return entity

#********************************************PUT************************************************* 
@route('/expenditure', method='PUT')
def put_expenditure():
    data = request.body.readline().decode('utf8')
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    #print(entity)
    if '_id' not in entity:
        abort(400, 'No _id specified')
    try:
       print(list(entity.keys()))
       aaa=str(list(entity.keys())[1])
       result=db['expenditure'].update({"_id": ObjectId(entity['_id'])}, {"$set":{list(entity.keys())[1]: entity[list(entity.keys())[1]]}})
       
       print(result)
    except pymongo.errors.WriteError as ve:
        abort(400, str(ve))
    return result
       

#********************************************POST*************************************************        
@route('/expenditure', method='POST')
def post_expenditure():
    data = request.body.readline().decode('utf8')
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    print(entity)
    #if '_id' not in entity:
    #    abort(400, 'No _id specified')
 #   if '_id_user' not in entity:
  #      abort(400, 'No _id_user specified')
    try:
        db['expenditure'].save(entity)
    except pymongo.errors.WriteError as ve:
        abort(400, str(ve))
#********************************************GET*************************************************       
@route('/expenditure', method='GET')
def get_all_expenditure():
    entity = db['expenditure'].find()
    if not entity:
        abort(404, 'DB is empty')
    #print(json.loads("{\"1\":\"2\"}"))
    return json.loads(entity_to_str(entity))


#get expenditure for _id_user   
@route('/expenditure/:id', method='GET')
def get_expenditure(id):
    entity = db['expenditure'].find_one({'_id': id})
    print(entity)
    if not entity:
        abort(404, 'No document with id %s' % id)
    return entity

#get user for id
@route('/expenditure/user/:id', method='GET')
def get_expenditure_for_user(id):
    entity = db['expenditure'].find_one({'_id_user':id})
    print(entity)
    if not entity:
        abort(404, 'No document with id %s' % id)
    return entity
#********************************************DELETE*************************************************    
@route('/expenditure/:id', method='DELETE')
def delete_expenditure(id):
    entity = db['expenditure'].remove({'_id':id})
    #if not entity:
        #abort(404, 'No document with id %s' % id)
    #result = db['expenditure'].remove({'_id_user':id})
    return entity
 
@route('/expenditure/all/', method='DELETE')
def delete_expenditure_all():
    try:
        entity = db['expenditure'].remove({})
    except:
        print ('error/exception')
    return entity


run(host='localhost', port=8080)
#application = bottle.default_app()
#from paste import httpserver
#httpserver.serve(application, host='0.0.0.0', port=80)