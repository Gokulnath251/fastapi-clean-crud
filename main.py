from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, get_db

# Create the database tables on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product API with Clean Architecture")

@app.post("/products", response_model=schemas.ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.ProductDB(
        name=product.name,
        price=product.price,
        cost_price=product.cost_price,
        in_stock=product.in_stock
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products", response_model=list[schemas.ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return db.query(models.ProductDB).all()

@app.get("/products/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.ProductDB).filter(models.ProductDB.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

@app.put("/products/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, product_update: schemas.ProductUpdate, db: Session = Depends(get_db)):
    product = db.query(models.ProductDB).filter(models.ProductDB.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    update_data = product_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(product, field, value)
        
    db.commit()
    db.refresh(product)
    return product

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.ProductDB).filter(models.ProductDB.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    db.delete(product)
    db.commit()
    return None
