from fastapi import APIRouter, Depends
from src.database import get_db
from src.modules import crud
from src.modules.models import Item
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/items/", response_model=Item)
def create_item(item: Item, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@router.get("/items/", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_items(db=db, skip=skip, limit=limit)

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    return crud.get_item(db=db, item_id=item_id)

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item, db: Session = Depends(get_db)):
    return crud.update_item(db=db, item_id=item_id, item=item)

@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    crud.delete_item(db=db, item_id=item_id)
    return {"message": "Item deleted successfully"}