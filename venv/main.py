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
collection = database['customers']

# gives the first item in the collection and creates the collection in the database
customer_dict = {'name': 'Arthur', 'address': 'lemoyne'}
test1 = collection.insert_one(customer_dict)

print('test1:', test1)
print('test1.id:', test1.inserted_id)

# prints the names of the different collections in the database
print('list of collections in the database:', database.list_collection_names())