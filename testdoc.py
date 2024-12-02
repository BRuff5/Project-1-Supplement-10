import pytest
from unittest.mock import MagicMock

from main import generate_random_document


def test_generate_random_document():
    """Test the generate_random_document function."""
    document = generate_random_document()

    # Check if the document has the correct structure
    assert 'UUID' in document
    assert 'name' in document
    assert 'age' in document
    assert 'email' in document

    # Validate types
    assert isinstance(document['UUID'], str)
    assert isinstance(document['name'], str)
    assert isinstance(document['age'], int)
    assert isinstance(document['email'], str)

def test_mongo_insertion():
    """Test MongoDB document insertion using a mock."""
    # Mock the collection
    mock_collection = MagicMock()

    # Generate a document and insert into the mocked collection
    document = generate_random_document()
    mock_collection.insert_one = MagicMock(return_value=None)  # Mock the insert_one method

    # Perform insertion
    mock_collection.insert_one(document)

    # Assert the insertion was called with the generated document
    mock_collection.insert_one.assert_called_once_with(document)
