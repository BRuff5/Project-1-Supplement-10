import pytest
from unittest.mock import MagicMock
from main import (
    generate_random_document,
    save_document,
    find_document_by_uuid,
    update_document_field,
    delete_document_by_uuid,
)

@pytest.fixture
def mock_collection():
    """Fixture for mocking MongoDB collection."""
    return MagicMock()

def test_generate_random_document():
    """Test the generate_random_document function."""
    document = generate_random_document()

    # Validate document structure
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
    mock_collection.insert_one = MagicMock()

    # Generate a document and save it
    document = generate_random_document()
    result = save_document(document)

    # Validate UUID is returned
    assert result == document['UUID']

    # Validate the document was inserted
    mock_collection.insert_one.assert_called_once_with(document)

def test_find_document_by_uuid(mock_collection):
    """Test the find_document_by_uuid function."""
    # Create a mock document
    document = generate_random_document()

    # Mock the find_one method
    mock_collection.find_one = MagicMock(return_value=document)

    # Retrieve the document by UUID
    result = find_document_by_uuid(document['UUID'])

    # Validate the retrieved document
    assert result == document

    # Validate the query
    mock_collection.find_one.assert_called_once_with({'UUID': document['UUID']})

def test_update_document_field(mock_collection):
    """Test the update_document_field function."""
    uuid = "test-uuid"
    field = "name"
    value = "Updated Name"

    # Mock the update_one method
    mock_collection.update_one = MagicMock(return_value=MagicMock(modified_count=1))

    # Perform the update
    result = update_document_field(uuid, field, value)

    # Validate the update result
    assert result is True

    # Validate the update query
    mock_collection.update_one.assert_called_once_with(
        {'UUID': uuid}, {'$set': {field: value}}
    )

def test_delete_document_by_uuid(mock_collection):
    """Test the delete_document_by_uuid function."""
    uuid = "test-uuid"

    # Mock the delete_one method
    mock_collection.delete_one = MagicMock(return_value=MagicMock(deleted_count=1))

    # Perform the deletion
    result = delete_document_by_uuid(uuid)

    # Validate the delete result
    assert result is True

    # Validate the delete query
    mock_collection.delete_one.assert_called_once_with({'UUID': uuid})
