import uuid
from pymongo import MongoClient

# MongoDB Configuration
mongo_uri = 'mongodb://localhost:27017/'
db_name = 'mydatabase'
collection_name = 'mycollection'

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client[db_name]
collection = db[collection_name]

def generate_random_document() -> dict:
    """
    Generate a random MongoDB document with a UUID and predefined fields.

    Returns:
        dict: A dictionary representing the MongoDB document, including:
            - UUID: A unique identifier (string).
            - name: A string field.
            - age: An integer field.
            - email: A string field.
    """
    document = {
        'UUID': str(uuid.uuid4()),  # Generate a version 4 UUID
        'name': 'Bryson Ruff',
        'age': 20,
        'email': 'bfirst86@gmail.com'
    }
    return document

def save_document(document: dict) -> str:
    """
    Save a MongoDB document to the database.

    Args:
        document (dict): The MongoDB document to save.

    Returns:
        str: The UUID of the saved document.
    """
    collection.insert_one(document)  # Insert document into the collection
    return document['UUID']  # Return the UUID of the saved document

def find_document_by_uuid(uuid: str) -> dict:
    """
    Find a MongoDB document by its UUID.

    Args:
        uuid (str): The UUID to search for.

    Returns:
        dict or None: The found document, or None if not found.
    """
    return collection.find_one({'UUID': uuid})

def update_document_field(uuid: str, field: str, value) -> bool:
    """
    Update a specific field in a MongoDB document identified by UUID.

    Args:
        uuid (str): The UUID of the document to update.
        field (str): The field to update.
        value: The new value for the specified field.

    Returns:
        bool: True if a document was updated; False otherwise.
    """
    result = collection.update_one(
        {'UUID': uuid},
        {'$set': {field: value}}
    )
    return result.modified_count > 0

def delete_document_by_uuid(uuid: str) -> bool:
    """
    Delete a MongoDB document identified by UUID.

    Args:
        uuid (str): The UUID of the document to delete.

    Returns:
        bool: True if a document was deleted; False otherwise.
    """
    result = collection.delete_one({'UUID': uuid})
    return result.deleted_count > 0

if __name__ == "__main__":
    # Demonstrate functionality

    doc = generate_random_document()
    uuid_str = save_document(doc)
    print(f"Document saved with UUID: {uuid_str}")

    #Find the document
    found_doc = find_document_by_uuid(uuid_str)
    print(f"Found document: {found_doc}")

    # Update
    updated = update_document_field(uuid_str, 'age', 21)
    print(f"Document updated: {updated}")

    # Delete 
    deleted = delete_document_by_uuid(uuid_str)
    print(f"Document deleted: {deleted}")
