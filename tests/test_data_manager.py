import pytest
from app.data_manager import DataManager



@pytest.fixture
def data_manager():
    return DataManager()

def test_add_user(data_manager):
    user = data_manager.add_user("Alice", 25)
    assert user["name"] == "Alice"
    assert user["age"] == 25
    assert len(data_manager.get_users()) == 1

def test_get_users(data_manager):
    data_manager.add_user("Bob", 30)
    users = data_manager.get_users()
    assert len(users) == 1
    assert users[0]["name"] == "Bob"

def test_delete_user(data_manager):
    data_manager.add_user("Charlie", 22)
    assert data_manager.delete_user(1) == True
    assert data_manager.delete_user(99) == False
