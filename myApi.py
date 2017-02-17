import json
import bson
import bottle
from bottle import post, route, run, request, abort,response
from pymongo import Connection
import pymongo
#from income_to import my_data_to_str, is_number
from bson.objectid import ObjectId
#import os
#import http.cookies
import logging
from cork import Cork
from beaker.middleware import SessionMiddleware
from cork.backends import MongoDBBackend
#import datetime

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False



#--------------
logging.basicConfig(format='localhost - - [%(asctime)s] %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)
bottle.debug(True)

# Use users.json and roles.json in the local example_conf directory
'''def populate_mongodb_backend():
    mb = MongoDBBackend(db_name='users_system', initialize=True)
    mb.users._coll.insert({
        "login": "admin",
        "email_addr": "admin@localhost.local",
        "desc": "admin test user",
        "role": "admin",
        "hash": "cLzRnzbEwehP6ZzTREh3A4MXJyNo+TV8Hs4//EEbPbiDoo+dmNg22f2RJC282aSwgyWv/O6s3h42qrA6iHx8yfw=",
        "creation_date": "2012-10-28 20:50:26.286723"
    })
    mb.roles._coll.insert({'role': 'admin', 'val': 100})
    mb.roles._coll.insert({'role': 'editor', 'val': 60})
    mb.roles._coll.insert({'role': 'user', 'val': 50})
    return mb

mb = populate_mongodb_backend()'''
mb = MongoDBBackend(db_name='users_system', initialize=True)
aaa = Cork(backend=mb, email_sender='avsh_174@mail.ru', smtp_url='ssl://avsh_174@mail.ru:qwerty123456@smtp.mail.ru:465')

# alias the authorization decorator with defaults
authorize = aaa.make_auth_decorator(fail_redirect="/login", role="user")


app = bottle.app()
session_opts = {
    'session.cookie_expires': True,
    'session.encrypt_key': 'Qwwwew123141*u',
    'session.httponly': True,
    'session.timeout': 3600 * 24,  # 1 day
    'session.type': 'cookie',
    'session.validate_key': True,
}
app = SessionMiddleware(app, session_opts)


# #  Bottle methods  # #

def postd():
    return bottle.request.forms


def post_get(name, default=''):
    print(bottle.request)
    return bottle.request.POST.get(name, default).strip()


@post('/login')
def login():
    """Authenticate users"""
    username = post_get('username')
    password = post_get('password')
    print("str name "+str(username))
    print(password)
    aaa.login(username, password, success_redirect='/', fail_redirect='/sorry_page')

@route('/')
def index():
    """Only authenticated users can see this"""
    aaa.require(fail_redirect='/sorry_page')
    return 'Welcome! %s ' % aaa.current_user.username


@bottle.route('/logout')
def logout():
    aaa.logout(success_redirect='/login')
    
@route('/sorry_page')
def sorry_page():
    """Serve sorry page"""
    return '<p>Sorry, you are not authorized to perform this action</p>'

@bottle.post('/register')
def register():
    """Send out registration email"""
    aaa.register(post_get('username'), post_get('password'), post_get('email_address'))
    return 'Please check your mailbox.'


@bottle.route('/validate_registration/:registration_code')
def validate_registration(registration_code):
    """Validate registration, create user account"""
    aaa.validate_registration(registration_code)
    return 'Thanks. <a href="/login">Go to login</a>'

    
@bottle.route('/login')
@bottle.view('login_form')
def login_form():
    """Serve login form"""
    return {}
#--------------


@post("/user")
def foo():
    asd=request.forms.get("age")  # Получить содержимое одного поля age
    print(asd)
    print(request.get_cookie("name"))
    print("------------------------")
    print(str(request.headers['Host']))
    for i in request.headers:
        print(str(i))
    print("------------------------")
    d={}
    d['name']=request.forms.get("name")
    d['password']=request.forms.get("password")
    db['users'].save(d)
    response.set_cookie("name", "11111", secret='qwe')
    print(response._cookies['name'])
    return "Hello word"

#********************************************PUT**********************************
@route('/income', method='PUT')
def put_income():
    aaa.require(fail_redirect='/sorry_page')
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
    aaa.require(fail_redirect='/sorry_page')
    lwist1=['_id_user','sum','category','note','data','customer']
    data = request.body.readline().decode('utf8')
    print("------------------------")
    print(str(request.headers['Host']))
    for i in request.headers:
        print(str(i))
    print("------------------------")
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
    aaa.require(fail_redirect='/sorry_page')
    my_data = db['income'].find()
    l=[]
    for i in my_data:
        l.append(JSONEncoder().encode(i))
    if not my_data:
        abort(404, 'DB is empty')
    return l

#get income for _id   
@route('/income/:id', method='GET')
def get_income(id):
    aaa.require(fail_redirect='/sorry_page')
    print(id)
    try:
        my_data = db['income'].find_one({'_id': ObjectId(id)})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    print(my_data)
    if not my_data:
        abort(404, 'No document with id %s' % id)
    return JSONEncoder().encode(my_data)

#get user for id_user
@route('/income/user/:id', method='GET')
def get_income_for_user(id):
    aaa.require(fail_redirect='/sorry_page')
    my_data = db['income'].find({'_id_user':id})
    l=[]
    for i in my_data:
        l.append(JSONEncoder().encode(i))
    if not my_data:
        abort(404, 'DB is empty')
    return l
#********************************************DELETE*************************************************    
@route('/income/:id', method='DELETE')
def delete_income(id):
    aaa.require(fail_redirect='/sorry_page')
    try:
        my_data = db['income'].remove({'_id':ObjectId(id)})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    return my_data
 
@route('/income/all/', method='DELETE')
def delete_income_all():
    aaa.require(fail_redirect='/sorry_page')
    try:
        my_data = db['income'].remove({})
    except:
        print ('error/exception')
    return my_data

#********************************************PUT_expenditure************************************************* 
@route('/expenditure', method='PUT')
def put_expenditure():
    aaa.require(fail_redirect='/sorry_page')
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
    aaa.require(fail_redirect='/sorry_page')
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
    aaa.require(fail_redirect='/sorry_page')
    my_data = db['expenditure'].find()
    l=[]
    for i in my_data:
        l.append(JSONEncoder().encode(i))
    if not my_data:
        abort(404, 'DB is empty')
    return l

#get expenditure for _id
@route('/expenditure/:id', method='GET')
def get_expenditure(id):
    aaa.require(fail_redirect='/sorry_page')
    print(id)
    try:
        my_data = db['expenditure'].find_one({'_id': ObjectId(id)})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    print(type(my_data))
    if not my_data:
        abort(404, 'No document with id %s' % id)
    return JSONEncoder().encode(my_data)

#get user for id_user
@route('/expenditure/user/:id', method='GET')
def get_expenditure_for_user(id):
    aaa.require(fail_redirect='/sorry_page')
    my_data = db['expenditure'].find({'_id_user':id})
    l=[]
    for i in my_data:
        l.append(JSONEncoder().encode(i))
    if not my_data:
        abort(404, 'DB is empty')
    return l
#********************************************DELETE*************************************************    
@route('/expenditure/:id', method='DELETE')
def delete_expenditure(id):
    aaa.require(fail_redirect='/sorry_page')
    try:
        my_data = db['expenditure'].remove({'_id':ObjectId(id)})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    return my_data
 
@route('/expenditure/all/', method='DELETE')
def delete_expenditure_all():
    aaa.require(fail_redirect='/sorry_page')
    try:
        my_data = db['expenditure'].remove({})
    except:
        print ('error/exception')
    return my_data

#***************************************************************************************************
#********************************************PUT_customer************************************************* 
@route('/customer', method='PUT')
def put_customer():
    aaa.require(fail_redirect='/sorry_page')
    data = request.body.readline().decode('utf8')
    lwist1=['customer']
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

   # print("list_key"+str(list_key))
    #print(lwist1.count(list_key[0]))

    list_key.remove('_id')
    print("list_key"+str(list_key))
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
    aaa.require(fail_redirect='/sorry_page')
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
        
    try:
        db['customer'].save(my_data)
    except pymongo.errors.WriteError as ve:
        abort(400, str(ve))
    return JSONEncoder().encode(my_data)
#********************************************GET*************************************************       
@route('/customer', method='GET')
def get_all_customer():
    aaa.require(fail_redirect='/sorry_page')
    my_data = db['customer'].find()
    if not my_data:
        abort(404, 'DB is empty')
    l=[]
    for i in my_data:
        l.append(JSONEncoder().encode(i))
    if not my_data:
        abort(404, 'DB is empty')
    return l


#get customer for _id_user   
@route('/customer/:id', method='GET')
def get_customer(id):
    aaa.require(fail_redirect='/sorry_page')
    print(id)
    try:
        my_data = db['customer'].find_one({'_id': ObjectId(id)})
        #my_data = db['customer'].find({'customer':id})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    l=[]
    for i in my_data:
        l.append(JSONEncoder().encode(i))
    if not my_data:
        abort(404, 'DB is empty')
    return l
#********************************************DELETE*************************************************    
@route('/customer/:id', method='DELETE')
def delete_customer(id):
    aaa.require(fail_redirect='/sorry_page')
    try:
        my_data = db['customer'].remove({'_id':ObjectId(id)})
    except bson.errors.BSONError:
        abort(400, '_id is wrong')
    return my_data
 
@route('/customer/all/', method='DELETE')
def delete_customer_all():
    aaa.require(fail_redirect='/sorry_page')
    try:
        my_data = db['customer'].remove({})
    except:
        print ('error/exception')
    return my_data
    
from bottle import static_file
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./frontend/public/')
    
connection = Connection('localhost', 27017)
db = connection.mydatabase
bottle.debug(True)
run(app=app,host='localhost', port=8080,quiet=False)
#application = bottle.default_app()
#from paste import httpserver
#httpserver.serve(application, host='0.0.0.0', port=80)