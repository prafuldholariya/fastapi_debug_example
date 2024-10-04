# main.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import uvicorn

from database import SessionLocal, engine
from models import Item
from schemas import ItemCreate, ItemResponse

# Create the database tables
Item.__table__.create(bind=engine, checkfirst=True)

app = FastAPI()


# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/', response_class=HTMLResponse)
async def home():
    return '''
            <h1> Home Page </h1>
            <a href='http://localhost:5000/docs'>http://localhost:5000/docs </a>
            '''


@app.post("/items/", response_model=ItemResponse)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/items/", response_model=list[ItemResponse])
async def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = db.query(Item).offset(skip).limit(limit).all()
    return items


@app.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.model_dump().items():
        setattr(db_item, key, value)
    db.commit()
    return db_item


@app.delete("/items/{item_id}", response_model=ItemResponse)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)
