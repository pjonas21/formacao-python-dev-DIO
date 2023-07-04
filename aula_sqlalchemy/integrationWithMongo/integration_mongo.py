import datetime
import pprint

import pymongo as pyM

cliente = pyM.MongoClient(
    "mongodb+srv://<username>:<password>@clusterlearrn.z1cmxtg.mongodb.net/?retryWrites=true&w=majority")

db = cliente.test
collection = db.test_collection
print(db.test_collection)


# preparacao de informacoes para banco de dados
post = {
    "author": "Mike",
    "text": "My first MongoDB application based on Python",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# criacao de uma collection (posts)
posts = db.posts

# insercao dos dados na collection
post_id = posts.insert_one(post).inserted_id

print(post_id)
print(posts)

# impressao formatada com pprint
pprint.pprint(db.posts.find_one())

# bulk insert
new_posts = [
    {
        "author": "Jonas",
        "text": "My second post",
        "tags": ["bulk", "insert"],
        "date": datetime.datetime.utcnow()
    },
    {
        "author": "Mark",
        "text": "Some text posted from Python APP",
        "title": "PythonApp",
        "tags": ["python", "app", "inserted"],
        "date": datetime.datetime.utcnow()
    }
]

result = posts.insert_many(new_posts)
print(result.inserted_ids)
print()
pprint.pprint(db.posts.find_one({"author": "Jonas"}))


