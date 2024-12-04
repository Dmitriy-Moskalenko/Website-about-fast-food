from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

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
    return db.query(Product).all()


# Функция для создание продукта
@app.post('/create_product/')
async def create_product(product: ProductConfig, db: Session = Depends(get_db)):
    create_prod = Product(title=product.title, description=product.description,
                          category_id=product.category_id)

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


# Функция для изменения записи
@app.put('/edit_product_all/{product_id}/')
async def edit_product_all(product_id: int, product: ProductConfig, db: Session = Depends(get_db)):
    edit_prod = db.query(Product).filter(Product.id == product_id).first()

    edit_prod.title = product.title
    edit_prod.description = product.description
    edit_prod.category_id = product.category_id

    db.commit()
    db.refresh(edit_prod)

    return edit_prod


# Функция для удаления продукта
@app.delete('/delete_product/{product_id}/')
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    delete_prod = db.query(Product).filter(Product.id == product_id).first()

    db.delete(delete_prod)
    db.commit()

    return "Продукт успешно удалён"


# Функция для удаления категории
@app.delete('/delete_category/{cat_id}/')
async def delete_category(cat_id: int, db: Session = Depends(get_db)):
    delete_cat = db.query(Category).filter(Category.id == cat_id).first()

    db.delete(delete_cat)
    db.commit()

    return "Категория успешно удалена"


# # Функция для изменения конкретного поля
# @app.patch('/edit_product/{product_id}/')
# async def edit_product(product_id: int, product: ProductConfig, db: Session = Depends(get_db)):
#     edit_prod = db.query(Product).filter(Product.id == product_id).first()
#
#     if product.title is not None:
#         edit_prod.title = product.title
#     if product.description is not None:
#         edit_prod.description = product.description
#     if product.category_id is not None:
#         edit_prod.category_id = product.category_id
#
#     db.commit()
#     db.refresh(edit_prod)
#     return jsonable_encoder(edit_prod)
