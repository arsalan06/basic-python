import pymongo
if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['test_database']
    collection = db["test-collection"]
    post = {
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
    }
    posts = db.posts
    post_id = posts.insert_one(post).inserted_id
    post_id
