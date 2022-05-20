from sqlalchemy.orm import session

from src import models


def get_product(db: session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_last_log(db: session):
    last_log = db.query(models.Log).order_by(models.Log.time_stamp.desc()).limit(1).first()
    if last_log:
        return last_log
    else:
        return 1
