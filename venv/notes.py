import pymongo
from pymongo.server_api import ServerApi
import password

'''setting up database'''

uri = 'mongodb+srv://' + password.mongodb_username + ':' + password.mongodb_password + '@cluster0.2o89z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
# print(uri)
# i think thats how you dont leak your api keys on git hub

# creates a new client and connects to the server
client = pymongo.MongoClient(uri, server_api=ServerApi('1'))

# sends a ping if a connection is established
try:
    client.admin.command('ping')
    print('MongoDB database successfully connected.')
    print('-----------------------------------------------')
except Exception as e:
    print(e)

# sets up the database and the collections(customers) ie. entity
database = client['test_database']
collection_customers = database['customers']

# creating the first document in the collection creates the collection
customer_dict = {'name': 'Arthur', 'address': 'Lemoyne'}  # a record (document)
test1 = collection_customers.insert_one(customer_dict)  # inserts customer_dict into the collection test1

# print('test1:', test1)
# print('test1.id:', test1.inserted_id)

# prints the names of the different collections in the database
print('list of collections in the database:', database.list_collection_names())

# inserting multiple documents into a collection
customer_dict_list = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]  # lifted directly from w3 school

# inserts the whole list of documents into the collection
# test2 = collection_customers.insert_many(customer_dict_list)
# print('test2:', test2)

# inserting documents with specified ids
specific_id_customer = {'_id': 1909, 'name': 'John', 'address': 'Mexico'}
try:
    test3 = collection_customers.insert_one(specific_id_customer)
    print('test3.id:', test3.inserted_id)
except Exception as e:
    print('ERROR OCCURRED:', e)
# it seems that you cannot have two documents with the same id and running the program again will result in an error

"""finding stuff in database"""

#  finding any and all records in a collection
find1 = collection_customers.find_one()  # finds the first instance of the record that matches the description
print('find1:', find1)

counter = 0
for i in collection_customers.find(): # finds all occurrences of the records that match the description
    counter += 1
    print(f'find2.{counter}: {i}')

# only showing selected fields of records
counter = 0
for i in collection_customers.find({},{'address':1}):  # only show address and nothing else
    counter += 1
    print(f'find3.{counter}:', i)
counter = 0
for i in collection_customers.find({}, {'address':0}):  # show everything but address
    counter += 1
    print(f'find4.{counter}:', i)

# querying with find function
query1 = collection_customers.find({'address':'Lemoyne'}, {'address':1})  # only shows id and address of people whose address is in Lemonyne
counter = 0
for i in query1:
    counter += 1
    print(f'query1.{counter}:', i)

# collection_customers.insert_one({'name':'Zeph', 'address':'z street'})
query2 = collection_customers.find_one({'address': {'$gt': 'y'}})  # finds fist instance whose address starts with a letter larger than 'y'
print('query2:', query2)  # case sensitive

query3 = collection_customers.find_one({'name': {'$regex': '^M'}})  # finds first instance of the person whose name starts with M
print('query3:', query3)  # regular expression only works on strings

"""sorting stuff in database"""
