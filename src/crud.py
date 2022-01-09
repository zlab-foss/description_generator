from sqlalchemy.orm import session

from src import models


def get_product(db: session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()
