from sqlalchemy.orm import Session
from src.modules.models import Item, ItemInDB
from src.database import SessionLocal

# Ensure that the function names are unique

def get_item(db: Session, item_id: int) -> ItemInDB:
    return db.query(ItemInDB).filter(ItemInDB.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 10) -> list[ItemInDB]:
    return db.query(ItemInDB).offset(skip).limit(limit).all()

def create_item(db: Session, item: Item) -> ItemInDB:
    db_item = ItemInDB(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Ensure that the update_item function is unique

def update_item(db: Session, item_id: int, item: Item) -> ItemInDB:
    db_item = db.query(ItemInDB).filter(ItemInDB.id == item_id).first()
    if db_item:
        for key, value in item.dict().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int) -> ItemInDB:
    db_item = db.query(ItemInDB).filter(ItemInDB.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item