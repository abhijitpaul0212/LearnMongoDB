# LearnMongoDB

## NoSQL
* NoSQL databases (aka "not only SQL") are non-tabular databases and store data differently than relational tables. 
* NoSQL databases come in a variety of types based on their data model.
* The main types are document, key-value, wide-column, and graph. 
* They provide flexible schemas and scale easily with large amounts of data and high user loads.

## MongoDB
* MongoDB is a source-available cross-platform document-oriented database program.
* Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas.


## Features
* MongoDB uses Mozilla's SpiderMonkey JavaScript Engine
* MongoDB is a document based database which is different from relational database.
* Database has Collections (i.e Tables)
* Collections contains Documents (i.e Records)
* Documents in Database are stored in BSON format 
* Binary JSON (BSON) data type is the binary representation of a JSON data type format for serializing JSON documents
* Extended JSON is used to represent/read BSON data types


## Types of Databases
1. Relational:
    * SQL DB
    * Data is stored in relational tables comprising of Rows & Columns
    * It is mandatory to have fixed schema
2. Document
    * NoSQL DB
    * Data is stored in documents.
    * Its not mandatyory to have same schema for all documents


## JSON data Type
https://chistadata.com/wp-content/uploads/2022/06/image_2022-06-07_202609039-1536x725.png


## BSON data Type
https://f4n3x6c5.stackpathcdn.com/article/datatypes-in-mongodb/Images/image1.png


## MacOS 
### Launch Terminal
* Intall MongoDB CLI using --> brew install mongodb-atlas
* Run --> atlas auth login 
* Provide the auth-key for Atlas User authentication using the Atalas Cloud account
* Run --> atlas. (The response includes available commands and options for the Atlas CLI)


## To view list of Atlas Cluster
* atlas cluster list

## To view the connection String
* atlas clusters connectionStrings describe Cluster0

## Installed Mongosh
1. Open .zshrc file nano $HOME/.zshrc
2. You will see the commented $PATH variable here
3. export PATH=$HOME/bin:/usr/local/bin:/Users/ebin/Documents/Softwares/mongoDB/bin:$PATH
4. Activate the change source $HOME/.zshrc

## Use Mongosh to create Database & Collections
* show databases
* use forum
* db.createCollection('posts')
* show collections

## Insert Documents
* create a JSON object for a document, say doc1={postId: NumberInt(3511),shared: false};, doc2={postId: NumberInt(3511),shared: false};
* db.posts.insertOne(doc1)
* db.posts.insertMany([doc1, doc2])

## Find Documents
* db.getCollection('posts').find({})
* db.getCollection('posts').findOne({postId: 3015})
* db.getCollection('posts').find({"author.name": "Emily Watson"})
* db.getCollection('posts').find({tags: "programming"})


## Query Operators
* $or
* $and
* $eq
* $ne
* $lt
* $gt
* $in
* $nin
* $regex

* db.getCollection('posts').find({comments: {$gt: 0}})
* db.getCollection('posts').find({$and: [{comments: {$lt: 5}}, {comments: {$gt: 0}}]})
* db.getCollection('posts').find({ tags: {$in: ["programming", "coding"]}})


## Helper Methods
* sort() --> db.getCollection('posts').find({}).sort({comments: 1}). #here 1 means ascending sort & -1 means decending sort
* limit() --> db.getCollection('posts').find({}).limit(2)
* skip() --> db.getCollection('posts').find({}).skip(3)


## Update Operators
* $set
* $unset
* $inc
* $rename
* $currentDate
* $addToSet

## Update documents
* updateOne()
* updateMany()
* Args: <query>, <update>, <options>
   
* db.posts.updateOne({postId: 2618}, {$set: {shared: true}})  --> # here we are querying postId who's value is 2618 and setting shared=True
* db.posts.updateMany({tags: []}, {$unset: {tags: 1}})
* db.posts.updateMany({postId: 8451}, {$inc: {comments: 1}})  
   
   
## Delete Documents
* deleteOne({query})
* deleteMany({query})

* db.getCollection('posts').deleteOne({postId: 1111}
* db.getCollection('posts').deleteMany({title: {$exists: false}})


## Aggregation Framework
Aggregation in MongoDB allows for the transforming of data and results in a more powerful fashion than from using the find() command. Through the use of multiple stages and expressions, you are able to build a "pipeline" of operations on your data to perform analytic operations.
   
### Aggregating
* db.posts.aggregate([{$group: {_id: "$author.name"}}])

### Indexes
* db.posts.getIndexes()
