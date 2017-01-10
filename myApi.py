import json
#import bottle
from bottle import route, run, request, abort
from pymongo import Connection
 
connection = Connection('localhost', 27017)
db = connection.mydatabase
 
#entity = db['documents'].find_one({'_id':'doc1'})
#print(entity)
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
       #coll.update({"name": "Петр"}, {"surname": "Новосельцев", "age": 25})
       db['income'].update({"_id": entity['_id']}, {"name": entity['name']})
       
       print(entity['_id'])
    except ValidationError as ve:
        abort(400, str(ve))
        
@route('/income', method='POST')
def post_document():
    data = request.body.readline().decode('utf8')
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    #print(entity)
    if '_id' not in entity:
        abort(400, 'No _id specified')
 #   if '_id_income' not in entity:
  #      abort(400, 'No _id_income specified')
    try:
        db['income'].save(entity)
    except ValidationError as ve:
        abort(400, str(ve))
#********************************************GET*************************************************       
@route('/income', method='GET')
def get_all_income():
    entity = db['income'].find()
    for i in entity:
        print(i)
    print(entity)
    if not entity:
        abort(404, 'DB is empty')
    return entity

#get income for _id_income   
@route('/income/:id', method='GET')
def get_income(id):
    entity = db['income'].find_one({'_id_income':id})
    print(entity)
    if not entity:
        abort(404, 'No document with id %s' % id)
    return entity

#get user for id    
@route('/income/user/:id_user', method='GET')
def get_income_for_user(id):
    entity = db['income'].find_one({'_id':id})
    print(entity)
    if not entity:
        abort(404, 'No document with id %s' % id)
    return entity
    
@route('/income/:id_income', method='DELETE')
def delete_income(id):
    entity = db['income'].remove({'_id_income':id})
    if not entity:
        abort(404, 'No document with id_income %s' % id)
    result = db['income'].remove({'_id_income':id})
    return result
 
run(host='localhost', port=8080)