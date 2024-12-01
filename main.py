from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session, joinedload

from database import session_local, base, engine
from models import Product, Category
from config import ProductConfig, CategoryConfig

app = FastAPI()

# Создаём таблицы
base.metadata.create_all(bind=engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


# Функция для просмотра всех продуктов
@app.get('/')
async def get_all_products(db: Session = Depends(get_db)):
    try:
        return db.query(Product).options(joinedload(Product.category)).all()
    except:
        return "База пуста"


# Функция для создание продукта
@app.post('/create_product/')
async def create_product(product: ProductConfig, db: Session = Depends(get_db)):
    create_prod = Product(title=product.title, description=product.description,
                          category_id=product.category.id)
    db.add(create_prod)
    db.commit()
    db.refresh(create_prod)

    return create_prod


# Функция для создание категории
@app.post('/create_category/')
async def create_category(category: CategoryConfig, db: Session = Depends(get_db)):
    create_cat = Category(title=category.title)
    db.add(create_cat)
    db.commit()
    db.refresh(create_cat)

    return create_cat