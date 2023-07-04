import pprint

import pymongo
import pymongo as pyM

cliente = pyM.MongoClient(
    "mongodb+srv://pjonas21:pjas@clusterlearrn.z1cmxtg.mongodb.net/?retryWrites=true&w=majority")

db = cliente.test

posts = db.posts
proflies = db.profiles
profile_user = db.profile_user

print(posts.delete_one({"author": "Mike"}))

posts.drop()

for post in posts.find({}).sort("date"):
    pprint.pprint(post)

print("\nQtde documentos na base de dados")
pprint.pprint(posts.count_documents({}))
