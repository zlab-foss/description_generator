import time
import json

from src import crud, models
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

session = SessionLocal()


init_id = 1

while(True):
    products = crud.get_product(session, init_id)
    if products:
        product_obj = products.__dict__
        if not product_obj['description']:
            if product_obj['attributes']:
                for attr in list(product_obj['attributes']):
                    print(f"attribute: {str(json.loads(attr)['value']).encode().decode('utf-8')}")
            else:
                init_id = init_id + 1
                time.sleep(1)
        else:
            init_id = init_id + 1
            time.sleep(1)
    else:
        init_id = init_id + 1
        time.sleep(1)
