import json
import bson
from bottle import route, run, request, abort
from pymongo import Connection
import pymongo
from income_to import my_data_to_str, is_number
from bson.objectid import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
###
#my_data = db['documents'].find_one({'_id':'doc1'})
#print(my_data)

connection = Connection('localhost', 27017)
db = connection.mydatabase

#********************************************PUT**********************************
@route('/income', method='PUT')
def put_income():
 
    data = request.body.readline().decode('utf8')
    lwist1=['_id_user','sum','category','note','data','customer','_id']

    if not data:
        abort(400, 'No data received')
    try:
        my_data = json.loads(data)
    except json.decoder.JSONDecodeError:
        abort(400, 'Wrong format')
    if '_id' not in my_data:
        abort(400, 'No _id specified') 
    try:
        tmp=db['income'].find_one({'_id': ObjectId(my_data['_id'])}) 
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    for i in list(my_data.keys()):
        if lwist1.count(i) == 0:
            abort(400, 'Wrong parameter %s' % i)
        else:
            if i!='_id':
                tmp[i]=my_data[i]     
    try:
        db['income'].save(tmp)
    except pymongo.errors.WriteError as ve:
        abort(400, str(ve))
    return JSONEncoder().encode(tmp)
#********************************************POST*************************************************        
@route('/income', method='POST')
def post_income():
    lwist1=['_id_user','sum','category','note','data','customer']
    data = request.body.readline().decode('utf8')
    print(data)
    if not data:
        abort(400, 'No data received')
    try:
        my_data = json.loads(data)
    except json.decoder.JSONDecodeError:
        abort(400, 'Wrong format')
    print(my_data)
    if '_id' in my_data:
        abort(400, 'Id generate auto')
    if '_id_user' not in my_data:
        abort(400, 'No _id_user specified')
    if 'sum' not in my_data:
        abort(400, 'No sum specified')
    if 'customer' not in my_data:
        abort(400, 'No customer specified')
    if is_number(my_data['sum'])== False:
        abort(400, 'sum is not int')
    #   if '_id_user' not in my_data:
    #      abort(400, 'No _id_user specified')
    #list_key=list(my_data.keys())
    for i in list(my_data.keys()):
        if lwist1.count(i) == 0:
            abort(400, 'Wrong parameter')
    try:
        db['income'].save(my_data)
    except pymongo.errors.WriteError as ve:
        abort(400, str(ve))
    return JSONEncoder().encode(my_data)
#********************************************GET*************************************************       
@route('/income', method='GET')
def get_all_income():
    my_data = db['income'].find()
    if not my_data:
        abort(404, 'DB is empty')
    #print(json.loads("{\"1\":\"2\"}"))
    #s=my_data_to_str(my_data)
    return my_data_to_str(my_data)

#get income for _id_user   
@route('/income/:id', method='GET')
def get_income(id):
    print(id)
    try:
        my_data = db['income'].find_one({'_id': ObjectId(id)})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    print(my_data)
    if not my_data:
        abort(404, 'No document with id %s' % id)
    return JSONEncoder().encode(my_data)

#get user for id
@route('/income/user/:id', method='GET')
def get_income_for_user(id):
    my_data = db['income'].find_one({'_id_user':id})
    print(my_data)
    if not my_data:
        abort(404, 'No document with id %s' % id)
    return JSONEncoder().encode(my_data)
#********************************************DELETE*************************************************    
@route('/income/:id', method='DELETE')
def delete_income(id):
    try:
        my_data = db['income'].remove({'_id':ObjectId(id)})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    #if not my_data:
        #abort(404, 'No document with id %s' % id)
    #result = db['income'].remove({'_id_user':id})
    return my_data
 
@route('/income/all/', method='DELETE')
def delete_income_all():
    try:
        my_data = db['income'].remove({})
    except:
        print ('error/exception')
    return my_data

#********************************************PUT_expenditure************************************************* 
@route('/expenditure', method='PUT')
def put_expenditure():
    data = request.body.readline().decode('utf8')
    lwist1=['_id_user','sum','category','note','data','customer','_id']
    if not data:
        abort(400, 'No data received')
    try:
        my_data = json.loads(data)
    except json.decoder.JSONDecodeError:
        abort(400, 'Wrong format')
    if '_id' not in my_data:
        abort(400, 'No _id specified')    
    try:
        tmp=db['expenditure'].find_one({'_id': ObjectId(my_data['_id'])})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    for i in list(my_data.keys()):
        if lwist1.count(i) == 0:
            abort(400, 'Wrong parameter %s' % i)
        else:
            if i!='_id':
                tmp[i]=my_data[i]  
    try:
        db['expenditure'].save(tmp)
    except pymongo.errors.WriteError as ve:
        abort(400, str(ve))
    return JSONEncoder().encode(tmp)
#********************************************POST*************************************************        
@route('/expenditure', method='POST')
def post_expenditure():
    lwist1=['_id_user','sum','category','note','data','customer']
    data = request.body.readline().decode('utf8')
    if not data:
        abort(400, 'No data received')
    try:
        my_data = json.loads(data)
    except json.decoder.JSONDecodeError:
        abort(400, 'Wrong format')
    print(my_data)
    if '_id' in my_data:
        abort(400, 'Id generate auto')
    if '_id_user' not in my_data:
        abort(400, 'No _id_user specified')
    if 'sum' not in my_data:
        abort(400, 'No sum specified')
    if 'customer' not in my_data:
        abort(400, 'No customer specified')
    if is_number(my_data['sum'])== False:
        abort(400, 'sum is not int')
    #   if '_id_user' not in my_data:
    #      abort(400, 'No _id_user specified')
    #list_key=list(my_data.keys())
    for i in list(my_data.keys()):
        if lwist1.count(i) == 0:
            abort(400, 'Wrong parameter')
    try:
        db['expenditure'].save(my_data)
    except pymongo.errors.WriteError as ve:
        abort(400, str(ve))
    return JSONEncoder().encode(my_data)
#********************************************GET*************************************************       
@route('/expenditure', method='GET')
def get_all_expenditure():
    my_data = db['expenditure'].find()
    if not my_data:
        abort(404, 'DB is empty')
    #print(json.loads("{\"1\":\"2\"}"))
    #s=my_data_to_str(my_data)
    #print(s)
    return my_data_to_str(my_data)

#get expenditure for _id_user   
@route('/expenditure/:id', method='GET')
def get_expenditure(id):
    print(id)
    try:
        my_data = db['expenditure'].find_one({'_id': ObjectId(id)})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    print(my_data)
    if not my_data:
        abort(404, 'No document with id %s' % id)
    return JSONEncoder().encode(my_data)

#get user for id
@route('/expenditure/user/:id', method='GET')
def get_expenditure_for_user(id):
    my_data = db['expenditure'].find_one({'_id_user':id})
    print(my_data)
    if not my_data:
        abort(404, 'No document with id %s' % id)
    return JSONEncoder().encode(my_data)
#********************************************DELETE*************************************************    
@route('/expenditure/:id', method='DELETE')
def delete_expenditure(id):
    try:
        my_data = db['expenditure'].remove({'_id':ObjectId(id)})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    #if not my_data:
        #abort(404, 'No document with id %s' % id)
    #result = db['expenditure'].remove({'_id_user':id})
    return my_data
 
@route('/expenditure/all/', method='DELETE')
def delete_expenditure_all():
    try:
        my_data = db['expenditure'].remove({})
    except:
        print ('error/exception')
    return my_data

#***************************************************************************************************
#********************************************PUT_customer************************************************* 
@route('/customer', method='PUT')
def put_customer():
    data = request.body.readline().decode('utf8')
    lwist1=['name']
    if not data:
        abort(400, 'No data received')
    try:
        my_data = json.loads(data)
    except json.decoder.JSONDecodeError:
        abort(400, 'Wrong format')
        
    if '_id' not in my_data:
        abort(400, 'No _id specified')
        
    list_key=list(my_data.keys())
    
    if len(list_key) > 2:
        abort(400, 'Many parameter')
        
    
    
    print("list_key"+str(list_key))
    print(lwist1.count(list_key[0]))
    
    list_key.remove('_id')
    print("list_key"+str(list_key))
    if lwist1.count(list_key[0]) == 0:
        abort(400, 'Wrong parameter')
    try:
        print(my_data.keys())
        result=db['customer'].update({"_id": ObjectId(my_data['_id'])}, {"$set":{list_key[0]: my_data[list_key[0]]}})
        my_data = db['customer'].find_one({'_id': ObjectId(my_data['_id'])})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    except json.decoder.JSONDecodeError:
        abort(400, '_id is wrong')
    print("put result "+str(result))
    return JSONEncoder().encode(my_data)
#********************************************POST*************************************************        
@route('/customer', method='POST')
def post_customer():
    data = request.body.readline().decode('utf8')
    if not data:
        abort(400, 'No data received')
    try:
        my_data = json.loads(data)
    except json.decoder.JSONDecodeError:
        abort(400, 'Wrong format')
    print(my_data)
    if '_id' in my_data:
        abort(400, 'Id generate auto')
    if 'customer' not in my_data:
        abort(400, 'No customer specified')
    list_key=list(my_data.keys())
    if len(list_key) > 1:
        abort(400, 'Many parameter')
 #   if '_id_user' not in my_data:
  #      abort(400, 'No _id_user specified')
    try:
        db['customer'].save(my_data)
    except pymongo.errors.WriteError as ve:
        abort(400, str(ve))
    return JSONEncoder().encode(my_data)
#********************************************GET*************************************************       
@route('/customer', method='GET')
def get_all_customer():
    my_data = db['customer'].find()
    if not my_data:
        abort(404, 'DB is empty')
    #print(json.loads("{\"1\":\"2\"}"))
    s=my_data_to_str(my_data)
    #print(s)
    return s

#get customer for _id_user   
@route('/customer/:id', method='GET')
def get_customer(id):
    print(id)
    try:
        my_data = db['customer'].find_one({'_id': ObjectId(id)})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    print(my_data)
    if not my_data:
        abort(404, 'No document with id %s' % id)
    return JSONEncoder().encode(my_data)
#********************************************DELETE*************************************************    
@route('/customer/:id', method='DELETE')
def delete_customer(id):
    try:
        my_data = db['customer'].remove({'_id':ObjectId(id)})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    #if not my_data:
        #abort(404, 'No document with id %s' % id)
    #result = db['customer'].remove({'_id_user':id})
    return my_data
 
@route('/customer/all/', method='DELETE')
def delete_customer_all():
    try:
        my_data = db['customer'].remove({})
    except:
        print ('error/exception')
    return my_data
    
    
run(host='localhost', port=8080)
#application = bottle.default_app()
#from paste import httpserver
#httpserver.serve(application, host='0.0.0.0', port=80)