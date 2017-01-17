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
def put_income():
    data = request.body.readline().decode('utf8')
    lwist1=['_id_user','sum','category','note','data','customer']
    if not data:
        abort(400, 'No data received')
    try:
        entity = json.loads(data)
    except json.decoder.JSONDecodeError:
        abort(400, 'Wrong format')
        
    if '_id' not in entity:
        abort(400, 'No _id specified')
        
    list_key=list(entity.keys())
    
    if len(list_key) > 2:
        abort(400, 'Many parameter')
        
    
    
    print("list_key"+str(list_key))
    print(lwist1.count(list_key[0]))
    
    list_key.remove('_id')
    print("list_key"+str(list_key))
    if lwist1.count(list_key[0]) == 0:
        abort(400, 'Wrong parameter')
    try:
        print(entity.keys())
        result=db['income'].update({"_id": ObjectId(entity['_id'])}, {"$set":{list_key[0]: entity[list_key[0]]}})
        entity = db['income'].find_one({'_id': ObjectId(entity['_id'])})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    except json.decoder.JSONDecodeError:
        abort(400, '_id is wrong')
    print("put result "+str(result))
    return JSONEncoder().encode(entity)
#********************************************POST*************************************************        
@route('/income', method='POST')
def post_income():
    data = request.body.readline().decode('utf8')
    if not data:
        abort(400, 'No data received')
    try:
        entity = json.loads(data)
    except json.decoder.JSONDecodeError:
        abort(400, 'Wrong format')
    print(entity)
    if '_id' in entity:
        abort(400, 'Id generate auto')
    if '_id_user' not in entity:
        abort(400, 'No _id_user specified')
    if 'sum' not in entity:
        abort(400, 'No sum specified')
    if 'customer' not in entity:
        abort(400, 'No customer specified')
 #   if '_id_user' not in entity:
  #      abort(400, 'No _id_user specified')
    try:
        db['income'].save(entity)
    except pymongo.errors.WriteError as ve:
        abort(400, str(ve))
    return JSONEncoder().encode(entity)
#********************************************GET*************************************************       
@route('/income', method='GET')
def get_all_income():
    entity = db['income'].find()
    if not entity:
        abort(404, 'DB is empty')
    #print(json.loads("{\"1\":\"2\"}"))
    s=entity_to_str(entity)
    print(s)
    return s

#get income for _id_user   
@route('/income/:id', method='GET')
def get_income(id):
    print(id)
    try:
        entity = db['income'].find_one({'_id': ObjectId(id)})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
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
    return JSONEncoder().encode(entity)
#********************************************DELETE*************************************************    
@route('/income/:id', method='DELETE')
def delete_income(id):
    try:
        entity = db['income'].remove({'_id':ObjectId(id)})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
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

#********************************************PUT_expenditure************************************************* 
@route('/expenditure', method='PUT')
def put_expenditure():
    data = request.body.readline().decode('utf8')
    lwist1=['_id_user','sum','category','note','data']
    if not data:
        abort(400, 'No data received')
    try:
        entity = json.loads(data)
    except json.decoder.JSONDecodeError:
        abort(400, 'Wrong format')
        
    if '_id' not in entity:
        abort(400, 'No _id specified')
        
    list_key=list(entity.keys())
    
    if len(list_key) > 2:
        abort(400, 'Many parameter')
        
    
    
    print("list_key"+str(list_key))
    print(lwist1.count(list_key[0]))
    
    list_key.remove('_id')
    print("list_key"+str(list_key))
    if lwist1.count(list_key[0]) == 0:
        abort(400, 'Wrong parameter')
    try:
        print(entity.keys())
        result=db['expenditure'].update({"_id": ObjectId(entity['_id'])}, {"$set":{list_key[0]: entity[list_key[0]]}})
        entity = db['expenditure'].find_one({'_id': ObjectId(entity['_id'])})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    except json.decoder.JSONDecodeError:
        abort(400, '_id is wrong')
    print("put result "+str(result))
    return JSONEncoder().encode(entity)
#********************************************POST*************************************************        
@route('/expenditure', method='POST')
def post_expenditure():
    data = request.body.readline().decode('utf8')
    if not data:
        abort(400, 'No data received')
    try:
        entity = json.loads(data)
    except json.decoder.JSONDecodeError:
        abort(400, 'Wrong format')
    print(entity)
    if '_id' in entity:
        abort(400, 'Id generate auto')
    if '_id_user' not in entity:
        abort(400, 'No _id_user specified')
    if 'sum' not in entity:
        abort(400, 'No sum specified')
    if 'customer' not in entity:
        abort(400, 'No customer specified')
 #   if '_id_user' not in entity:
  #      abort(400, 'No _id_user specified')
    try:
        db['expenditure'].save(entity)
    except pymongo.errors.WriteError as ve:
        abort(400, str(ve))
    return JSONEncoder().encode(entity)
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
    print(id)
    try:
        entity = db['expenditure'].find_one({'_id': ObjectId(id)})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    print(entity)
    if not entity:
        abort(404, 'No document with id %s' % id)
    return JSONEncoder().encode(entity)

#get user for id
@route('/expenditure/user/:id', method='GET')
def get_expenditure_for_user(id):
    entity = db['expenditure'].find_one({'_id_user':id})
    print(entity)
    if not entity:
        abort(404, 'No document with id %s' % id)
    return JSONEncoder().encode(entity)
#********************************************DELETE*************************************************    
@route('/expenditure/:id', method='DELETE')
def delete_expenditure(id):
    try:
        entity = db['expenditure'].remove({'_id':ObjectId(id)})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
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

#***************************************************************************************************
#********************************************PUT_customer************************************************* 
@route('/customer', method='PUT')
def put_customer():
    data = request.body.readline().decode('utf8')
    lwist1=['name']
    if not data:
        abort(400, 'No data received')
    try:
        entity = json.loads(data)
    except json.decoder.JSONDecodeError:
        abort(400, 'Wrong format')
        
    if '_id' not in entity:
        abort(400, 'No _id specified')
        
    list_key=list(entity.keys())
    
    if len(list_key) > 2:
        abort(400, 'Many parameter')
        
    
    
    print("list_key"+str(list_key))
    print(lwist1.count(list_key[0]))
    
    list_key.remove('_id')
    print("list_key"+str(list_key))
    if lwist1.count(list_key[0]) == 0:
        abort(400, 'Wrong parameter')
    try:
        print(entity.keys())
        result=db['customer'].update({"_id": ObjectId(entity['_id'])}, {"$set":{list_key[0]: entity[list_key[0]]}})
        entity = db['customer'].find_one({'_id': ObjectId(entity['_id'])})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    except json.decoder.JSONDecodeError:
        abort(400, '_id is wrong')
    print("put result "+str(result))
    return JSONEncoder().encode(entity)
#********************************************POST*************************************************        
@route('/customer', method='POST')
def post_customer():
    data = request.body.readline().decode('utf8')
    if not data:
        abort(400, 'No data received')
    try:
        entity = json.loads(data)
    except json.decoder.JSONDecodeError:
        abort(400, 'Wrong format')
    print(entity)
    if '_id' in entity:
        abort(400, 'Id generate auto')
    if 'customer' not in entity:
        abort(400, 'No customer specified')
    list_key=list(entity.keys())
    if len(list_key) > 1:
        abort(400, 'Many parameter')
 #   if '_id_user' not in entity:
  #      abort(400, 'No _id_user specified')
    try:
        db['customer'].save(entity)
    except pymongo.errors.WriteError as ve:
        abort(400, str(ve))
    return JSONEncoder().encode(entity)
#********************************************GET*************************************************       
@route('/customer', method='GET')
def get_all_customer():
    entity = db['customer'].find()
    if not entity:
        abort(404, 'DB is empty')
    #print(json.loads("{\"1\":\"2\"}"))
    s=entity_to_str(entity)
    print(s)
    return s

#get customer for _id_user   
@route('/customer/:id', method='GET')
def get_customer(id):
    print(id)
    try:
        entity = db['customer'].find_one({'_id': ObjectId(id)})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    print(entity)
    if not entity:
        abort(404, 'No document with id %s' % id)
    return JSONEncoder().encode(entity)
#********************************************DELETE*************************************************    
@route('/customer/:id', method='DELETE')
def delete_customer(id):
    try:
        entity = db['customer'].remove({'_id':ObjectId(id)})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    #if not entity:
        #abort(404, 'No document with id %s' % id)
    #result = db['customer'].remove({'_id_user':id})
    return entity
 
@route('/customer/all/', method='DELETE')
def delete_customer_all():
    try:
        entity = db['customer'].remove({})
    except:
        print ('error/exception')
    return entity
    
    
run(host='localhost', port=8080)
#application = bottle.default_app()
#from paste import httpserver
#httpserver.serve(application, host='0.0.0.0', port=80)