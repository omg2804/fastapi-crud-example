import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import Base, get_db
from src.modules.models import ItemInDB
from src.modules.crud import create_item, get_item, update_item, delete_item

DATABASE_URL = "sqlite:///./test.db"

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture()
def db_session(test_db):
    return test_db

def test_create_item(db_session):
    item_data = {'name': 'Test Item', 'description': 'A test item', 'price': 10.0, 'tax': 1.0}
    item = create_item(db_session, ItemInDB(**item_data))
    assert item.id is not None
    assert item.name == item_data['name']


def test_read_item(db_session):
    item_data = {'name': 'Test Item', 'description': 'A test item', 'price': 10.0, 'tax': 1.0}
    created_item = create_item(db_session, ItemInDB(**item_data))
    item = get_item(db_session, created_item.id)
    assert item.id == created_item.id
    assert item.name == created_item.name


def test_update_item(db_session):
    item_data = {'name': 'Test Item', 'description': 'A test item', 'price': 10.0, 'tax': 1.0}
    created_item = create_item(db_session, ItemInDB(**item_data))
    updated_data = {'name': 'Updated Item', 'description': 'An updated test item', 'price': 15.0, 'tax': 2.0}
    updated_item = update_item(db_session, created_item.id, ItemInDB(**updated_data))
    assert updated_item.name == updated_data['name']
    assert updated_item.price == updated_data['price']


def test_delete_item(db_session):
    item_data = {'name': 'Test Item', 'description': 'A test item', 'price': 10.0, 'tax': 1.0}
    created_item = create_item(db_session, ItemInDB(**item_data))
    result = delete_item(db_session, created_item.id)
    assert result is not None
    assert get_item(db_session, created_item.id) is None