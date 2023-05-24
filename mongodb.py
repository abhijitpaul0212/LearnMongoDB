### https://cloud.mongodb.com/v2/645cd8fe6e2b09237b148682#/clusters

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://root:root@cluster0.k3s4vuf.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

try:
    # Send a ping to confirm a successful connection
    status = client.admin.command('ping')
    print("Response: {}".format(status))
    
    
    # Create a new Database
    db = client.kaggle_iris
    print("Database name is {0}".format(db.name))
    
    # Print list of Database names  
    print("List of databases in MongoDB Cluster: {0}".format(client.list_database_names()))
    
    # Create a new Collection
    coll = db.iris
    
    # Print list of Collections in a particular Database 
    print("List of collections in Database {0}: {1}".format(db.name, db.list_collection_names()))

    # Documents in JSON format
    doc = {"sepalLength": 5.5, "sepalWidth": 2.4, "petalLength": 3.7, "petalWidth": 1.0, "species": "versicolor"}
    
    doc_list = [
    {"sepalLength": 5.1, "sepalWidth": 3.5, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
    {"sepalLength": 4.9, "sepalWidth": 3.0, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
    {"sepalLength": 4.7, "sepalWidth": 3.2, "petalLength": 1.3, "petalWidth": 0.2, "species": "setosa"},
    {"sepalLength": 4.6, "sepalWidth": 3.1, "petalLength": 1.5, "petalWidth": 0.2, "species": "setosa"},
    {"sepalLength": 5.0, "sepalWidth": 3.6, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
    {"sepalLength": 5.4, "sepalWidth": 3.9, "petalLength": 1.7, "petalWidth": 0.4, "species": "setosa"},
    {"sepalLength": 5.8, "sepalWidth": 2.6, "petalLength": 4.0, "petalWidth": 1.2, "species": "versicolor"},
    {"sepalLength": 5.0, "sepalWidth": 3.4, "petalLength": 1.5, "petalWidth": 0.2, "species": "setosa"},
    {"sepalLength": 4.4, "sepalWidth": 2.9, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
     {"sepalLength": 5.9, "sepalWidth": 3.0, "petalLength": 5.1, "petalWidth": 1.8, "species": "virginica"}]
    
    # insert_one() method returns a InsertOneResult object, which has a property, inserted_id, that holds the id of the inserted document
    coll.insert_one(doc)
    
    # insert_many() method take a list containing dictionaries with the data you want to insert as argument 
    # and returns a InsertManyResult object, which has a property, inserted_ids, that holds the ids of the inserted documents.
    coll.insert_many(doc_list)
    
    
    # find() method returns all occurrences in the selection
    print("List of documents in Collection {0}".format(coll.name))
    for x in coll.find():
        print(x)
    
    # find_one() method returns the first occurrence in the selection.
    print(coll.find_one())
    
    # update_one() is used to update a record. The first parameter of the update_one() method is a query object defining which document to update.
    query = {"sepalLength": 5.9}
    newvalues = {"$set": {"petalWidth": 11.9}}
    print("Document prior udapte: {0}".format(coll.find_one(query)))
    coll.update_one(query, newvalues)
    print("Document after udapte: {0}".format(coll.find_one(query)))
    
    
    # To delete one document, we use the delete_one() method.
    # The first parameter of the delete_one() method is a query object defining which document to delete.
    x = coll.delete_one({"sepalLength": 5.4})
    print(x.deleted_count, " documents deleted using delete_one()")
            
    # To delete more than one document, use the delete_many() method.
    # The first parameter of the delete_many() method is a query object defining which documents to delete.
    x = coll.delete_many({})  # Empty query means delete all collection
    print(x.deleted_count, " documents deleted using delete_many()")
    
except Exception as e:
    print(e)
