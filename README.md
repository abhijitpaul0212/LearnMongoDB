# LearnMongoDB

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
![image](https://github.com/abhijitpaul0212/LearnMongoDB/assets/9966441/185e81b8-9684-455e-8426-73e848a4a5d4)


## BSON data Type
![image](https://github.com/abhijitpaul0212/LearnMongoDB/assets/9966441/1a62995c-8c25-4475-94f3-c88640ec6c98)


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
<img width="576" alt="image" src="https://github.com/abhijitpaul0212/LearnMongoDB/assets/9966441/e89cbe7d-872a-467b-a0af-28ab56eb60b1">

* create a JSON object for a document, say doc1={postId: NumberInt(3511),shared: false};, doc2={postId: NumberInt(3511),shared: false};
* db.posts.insertOne(doc1)
* db.posts.insertMany([doc1, doc2])
<img width="631" alt="image" src="https://github.com/abhijitpaul0212/LearnMongoDB/assets/9966441/36a7ce87-3438-42a6-a77d-266eb03b2f18">

* db.getCollection('posts').find({})
* db.getCollection('posts').findOne({postId: 3015})
<img width="690" alt="image" src="https://github.com/abhijitpaul0212/LearnMongoDB/assets/9966441/0825134f-bf9d-4922-bd4f-1976ab0dce49">

* db.getCollection('posts').find({"author.name": "Emily Watson"})
* db.getCollection('posts').find({tags: "programming"})
<img width="772" alt="image" src="https://github.com/abhijitpaul0212/LearnMongoDB/assets/9966441/4fe18162-ca49-483f-bd26-c068c5090b45">


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
<img width="772" alt="image" src="https://github.com/abhijitpaul0212/LearnMongoDB/assets/9966441/a4ca9391-6469-4d13-9832-b46555743a07">

## Helper Methods
* sort() --> db.getCollection('posts').find({}).sort({comments: 1})
* limit() --> db.getCollection('posts').find({}).limit(2)
* skip() --> db.getCollection('posts').find({}).skip(3)

![image](https://github.com/abhijitpaul0212/LearnMongoDB/assets/9966441/af637c46-474b-4c15-a3a8-6e9dfc6d2e86)




