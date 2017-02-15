# Freecome
###Request Examples
* List of expenditure:
    * GET http://hostname.ru/expenditure/
* Expenditure for id:
    * GET http://hostname.ru/expenditure/:_id
    * Exemple http://hostname.ru/expenditure/588eb5e8ac2e8913548d11b4
* List of expenditure for id user
    * GET http://hostname.ru/expenditure/user/:user_id
* List of income:
    * GET http://hostname.ru/income/
* Income for id:
    * GET http://hostname.ru/income/:_id
    * Exemple http://hostname.ru/income/588eb5e8ac2e8913548d11b4
* List of income for id user
    * GET http://hostname.ru/income/user/:user_id		
* List of customer
    * GET http://hostname.ru/customer
* List of customer for id
    * GET http://hostname.ru/customer/:id
    * Example http://hostname.ru/customer/588eb5e8ac2e8913548d11b4
* Delete income
	* DELETE http://hostname.ru/expenditure/:_id
* Delete all income
	* DELETE http://hostname.ru/expenditure/all/
* Delete expenditure
	* DELETE http://hostname.ru/expenditure/:_id 
* Delete all expenditure
	* DELETE http://hostname.ru/expenditure/all/	
* Delete customer
	* DELETE http://hostname.ru/customer/:_id 
* Delete all customer
	* DELETE http://hostname.ru/customer/all/
	
* Add expenditure
	* POST http://hostname.ru/expenditure
		
     * Example request body:

     {"customer": "customer", "note": "note", "sum": "1000", "_id_user": "1"}
		 
		 * Example response body:

     {"customer": "customer", "note": "note", "sum": "1000", "_id_user": "1"}
###### required fields
		 ['_id_user','sum','category','note','data','customer'] 
		 
* Add income
	* POST http://hostname.ru/income
		
     * Exemple request body:

     {"customer": "customer", "note": "note", "sum": "1000", "_id_user": "1"}
		 
		 * Exemple response body:

     {"_id": "58804917ac2e892214f6424a","customer": "customer", "note": "note", "sum": "1000", "_id_user": "1"}
###### required field
['_id_user','sum','category','note','data','customer']

* Add customer
	* POST http://hostname.ru/customer
		
     * Exemple request body:

     {"customer": "customer"}
###### required field
['customer']

* Update expenditure
	* PUT http://hostname.ru/expenditure
		
     * Exemple request body:

     {"_id": "58804917ac2e892214f6424a","customer": "customer", "note": "note", "sum": "1000", "_id_user": "1"}
		 
		 * Exemple response body:

     {"_id": "58804917ac2e892214f6424a","customer": "customer", "note": "note", "sum": "1000", "_id_user": "1"}
		 
* Update income
	* PUT http://hostname.ru/income
		
     * Exemple request body:

     {"_id": "58804917ac2e892214f6424a","customer": "customer", "note": "note", "sum": "1000", "_id_user": "1"}
		 
		 * Exemple response body:

     {"customer": "qqq", "_id": "58a2d0aeac2e8914e86a09c7"}
	
* Update customer
	* PUT http://hostname.ru/customer
		
     * Exemple request body:

     {"customer": "change_customer", "_id": "58a2d0aeac2e8914e86a09c7"}
		 
		 * Exemple response body:

     {"customer": "change_customer", "_id": "58a2d0aeac2e8914e86a09c7"}

