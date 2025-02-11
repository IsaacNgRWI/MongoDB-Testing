import pymongo
from pymongo.server_api import ServerApi
import password

uri = 'mongodb+srv://' + password.mongodb_username + ':' + password.mongodb_password + '@cluster0.2o89z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
# print(uri)
# feels like an oversight how you could just print the uri and see the password

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

# gives the first item in the collection and creates the collection in the database
customer_dict = {'name': 'Arthur', 'address': 'lemoyne'}  # a record (document)
test1 = collection_customers.insert_one(customer_dict)

print('test1:', test1)
print('test1.id:', test1.inserted_id)

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
test2 = collection_customers.insert_many(customer_dict_list)
print('test2:', test2)

# inserting documents with specified ids
specific_id_customer = {'_id': 1909, 'name': 'John', 'address': 'Mexico'}
try:
    test3 = collection_customers.insert_one(specific_id_customer)
    print('test3.id:', test3.inserted_id)
except Exception as e:
    print('ERROR OCCURRED:', e)
# it seems that you cannot have two documents with the same id and running the program again will result in an error