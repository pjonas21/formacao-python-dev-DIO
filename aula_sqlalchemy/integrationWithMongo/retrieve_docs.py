import pprint

import pymongo
import pymongo as pyM

cliente = pyM.MongoClient(
    "mongodb+srv://pjonas21:pjas@clusterlearrn.z1cmxtg.mongodb.net/?retryWrites=true&w=majority")

db = cliente.test
posts = db.posts

print("Docs dentro de posts collection")
# for post in posts.find():
#     pprint.pprint(post)
# pprint.pprint([post for post in posts.find()])

print("\nQtde documentos na base de dados")
pprint.pprint(posts.count_documents({}))

print("\nQtde documento de um autor")
pprint.pprint(posts.count_documents({"author": "Jonas"}))

print("\nQtde documento com tag especifica")
pprint.pprint(posts.count_documents({"tags": "python"}))

print("\nReceuperando dados de maneira ordenada")
# pprint.pprint([post for post in posts.find({}).sort("date")])
# for post in posts.find({}).sort("date"):
#     pprint.pprint(post)

result = db.profiles.create_index([('author', pymongo.ASCENDING)], unique=True)

print(sorted(list(db.profiles.index_information())))

user_profile = [
    {'user_id': 211, 'name': 'pjonas'},
    {'user_id': 212, 'name': 'paulo'},
]

result = db.profile_user.insert_many(user_profile)

print("\nReceuperando nomes das colecoes armazenadas")
print(db.list_collection_names())
