import pymongo
from pymongo.server_api import ServerApi
import password

uri = 'mongodb+srv://' + password.mongodb_username + ':' + password.mongodb_password + '@cluster0.2o89z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
# print(uri)

# creates a new client and connects to the server
client = pymongo.MongoClient(uri, server_api=ServerApi('1'))

# sends a ping if a connection is established
try:
    client.admin.command('ping')
    print('MongoDB database successfully connected.')
except Exception as e:
    print(e)
