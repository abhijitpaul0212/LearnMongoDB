### https://cloud.mongodb.com/v2/645cd8fe6e2b09237b148682#/clusters

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://root:root@cluster0.k3s4vuf.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

data = {
    "name": "bishal",
    "email": "bishalranjandey@gmail.com",
    "surname": "dey"
    }

# Send a ping to confirm a successful connection
try:
    status = client.admin.command('ping')
    print("Response: {}".format(status))
    
    db1 = client.mongotest1  # Here mongotest1 is the name of the database
    print("Database name is {0}".format(db1.name))
    coll1 = db1.test  # Here test is the name of table
    coll1.insert_one(data)


    db2 = client['mongotest2']
    coll2 = db2['test']
    
    coll2.insert_one(data).inserted_id
    coll2.insert_one({'a': 1, 'b': 2}).inserted_id

    print(client.list_database_names())
    print(db1.list_collection_names())
    print(db2.list_collection_names())

    print("Done")
    
    
    # print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
    
