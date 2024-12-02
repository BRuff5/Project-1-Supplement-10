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
        'UUID': str(uuid.uuid4()),  # Generate UUID as a string
        'name': 'Bryson Ruff',
        'age': 20,
        'email': 'bfirst86@gmail.com'
    }
    return document

def save_document(document: dict) -> str:
    """Save the document to MongoDB
    Args:
        dict: The MongoDB document to save
    Returns:
        str: The UUID 
    """
    result = collection.insert_one(document)
    return document['UUID']  # Return the UUID the document saved

def find_document_by_uuid(uuid: str) -> dict:
    """Find a document by its UUID.
    Args:
        uuid: The UUID to find
    Returns:
        dict: the document found
    """
    return collection.find_one({'UUID': uuid}) 

def update_document_field(uuid: str, field: str, value) -> bool:
    """Update the field based of UUID
    Args:
        uuid (str): The UUID
        field (str): The field to update
        value: The new value for the specified field.
    Returns:
        bool: True if a document was updated; False otherwise.
    """
    result = collection.update_one(
        {'UUID': uuid},
        {'$set': {field: value}}
    )
    return result.modified_count > 0  # Return True if document was updated
