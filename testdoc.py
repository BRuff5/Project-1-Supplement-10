import pytest
from unittest.mock import MagicMock, patch
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
    with patch('main.collection') as mock_collection:
        yield mock_collection

def test_generate_random_document():
    """Test the generate_random_document function."""
    document = generate_random_document()

    # Check keys and types
    assert 'UUID' in document
    assert 'name' in document
    assert 'age' in document
    assert 'email' in document
    assert isinstance(document['UUID'], str)
    assert isinstance(document['name'], str)
    assert isinstance(document['age'], int)
    assert isinstance(document['email'], str)

def test_save_document(mock_collection):
    """Test the save_document function."""
    document = generate_random_document()
    mock_collection.insert_one.return_value = MagicMock()

    uuid = save_document(document)

    # Verify the UUID returned matches the document's UUID
    assert uuid == document['UUID']

    # Check if the insert operation was called with the document
    mock_collection.insert_one.assert_called_once_with(document)

def test_find_document_by_uuid(mock_collection):
    """Test the find_document_by_uuid function."""
    document = generate_random_document()
    mock_collection.find_one.return_value = document

    found_document = find_document_by_uuid(document['UUID'])

    # Verify the returned document matches the mock document
    assert found_document == document

    # Verify the correct query was executed
    mock_collection.find_one.assert_called_once_with({'UUID': document['UUID']})

def test_update_document_field(mock_collection):
    """Test the update_document_field function."""
    uuid = "test-uuid"
    field = "name"
    value = "Updated Name"
    mock_collection.update_one.return_value = MagicMock(modified_count=1)

    result = update_document_field(uuid, field, value)

    # Verify the result is True (document was updated)
    assert result is True

    # Verify the update operation was called correctly
    mock_collection.update_one.assert_called_once_with(
        {'UUID': uuid}, {'$set': {field: value}}
    )

def test_delete_document_by_uuid(mock_collection):
    """Test the delete_document_by_uuid function."""
    uuid = "test-uuid"
    mock_collection.delete_one.return_value = MagicMock(deleted_count=1)

    result = delete_document_by_uuid(uuid)

    # Verify the result is True (document was deleted)
    assert result is True

    # Verify the delete operation was called with the correct UUID
    mock_collection.delete_one.assert_called_once_with({'UUID': uuid})
