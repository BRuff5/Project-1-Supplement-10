import uuid
from pymongo import MongoClient

# MongoDB 
mongo_uri = 'mongodb://localhost:27017/'
db_name = 'mydatabase'
collection_name = 'mycollection'

# Connect 
client = MongoClient(mongo_uri)
db = client[db_name]
collection = db[collection_name]

def generate_random_document() -> dict:
    """Generate a random MongoDB - UUID.
    Args: Dictionarty
    Returns:
        dict: A dictionary representing the MongoDB document with a 'UUID', 'name', 'age', and 'email' fields.
    """
    document = {
        'UUID': str(uuid.uuid4()),  # Generate a version 4 UUID as a string
        'name': 'John Doe',
        'age': 30,
        'email': 'johndoe@example.com'
    }
    return document