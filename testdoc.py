import pytest
from unittest.mock import MagicMock

from main import find_document_by_uuid, generate_random_document, save_document


@pytest.fixture
def mock_collection():
    """Fixture for mocking MongoDB collection."""
    mock = MagicMock()
    return mock

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

def test_save_document(mock_collection):
    """Test the save_document function."""
    # Mock insertion
    mock_collection.insert_one = MagicMock(return_value=None)

    # Generate and save document
    document = generate_random_document()
    result = save_document(document)

    # Validate the UUID is returned
    assert result == document['UUID']

    # Assert the insert_one method was called with the document
    mock_collection.insert_one.assert_called_once_with(document)

def test_find_document_by_uuid(mock_collection):
    """Test the find_document_by_uuid function."""
    # Create a mock document
    document = generate_random_document()

    # Mock the find_one method to return the document
    mock_collection.find_one = MagicMock(return_value=document)

    # Retrieve the document by UUID
    result = find_document_by_uuid(document['UUID'])

    # Validate the retrieved document matches the expected document
    assert result == document

    # Assert find_one was called with the correct query
    mock_collection.find_one.assert_called_once_with({'UUID': document['UUID']})

