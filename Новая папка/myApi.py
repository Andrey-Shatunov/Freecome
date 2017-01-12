import json
#import bottle
from bottle import route, run, request, abort
from pymongo import Connection
from bson.json_util import dumps
from income_to import entity_to_str

connection = Connection('localhost', 27017)
db = connection.mydatabase
 
#entity = db['documents'].find_one({'_id':'doc1'})
#print(entity)
#********************************************PUT************************************************* 
@route('/income', method='PUT')
def put_document():
    data = request.body.readline().decode('utf8')
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    #print(entity)
    if '_id' not in entity:
        abort(400, 'No _id specified')
    try:
       db['income'].update({"_id": entity['_id']}, {"$set":{"note": entity['note']}})
       
       print(entity['_id'])
    except ValidationError as ve:
        abort(400, str(ve))
#********************************************POST*************************************************        
@route('/income', method='POST')
def post_document():
    data = request.body.readline().decode('utf8')
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    print(entity)
    if '_id' not in entity:
        abort(400, 'No _id specified')
 #   if '_id_user' not in entity:
  #      abort(400, 'No _id_user specified')
    try:
        db['income'].save(entity)
    except ValidationError as ve:
        abort(400, str(ve))
#********************************************GET*************************************************       
@route('/income', method='GET')
def get_all_income():
    entity = db['income'].find()
    if not entity:
        abort(404, 'DB is empty')
    return entity_to_str(entity)

#get income for _id_user   
@route('/income/:id', method='GET')
def get_income(id):
    entity = db['income'].find_one({'_id': id})
    print(entity)
    if not entity:
        abort(404, 'No document with id %s' % id)
    return entity

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
    db['expenditure'].update({"_id": entity['_id']}, {"$set":{"note": entity['note']}})
       

#********************************************POST*************************************************        
@route('/expenditure', method='POST')
def post_expenditure():
    data = request.body.readline().decode('utf8')
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    print(entity)
    if '_id' not in entity:
        abort(400, 'No _id specified')
 #   if '_id_user' not in entity:
  #      abort(400, 'No _id_user specified')
    try:
        db['expenditure'].save(entity)
    except ValidationError as ve:
        abort(400, str(ve))
#********************************************GET*************************************************       
@route('/expenditure', method='GET')
def get_all_expenditure():
    entity = db['expenditure'].find()
    if not entity:
        abort(404, 'DB is empty')
    return entity_to_str(entity)

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