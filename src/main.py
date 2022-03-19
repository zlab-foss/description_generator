import time
import json

from elasticsearch import Elasticsearch

from src import crud, models, preprocess
from src.database import SessionLocal, engine
from src.adapter import get_attribute_id

models.Base.metadata.create_all(bind=engine)

es = Elasticsearch(hosts=["elasticsearch:9200"],http_auth=("elastic", "changeme"))

session = SessionLocal()


init_id = 1

while(init_id<348817):
    products = crud.get_product(session, init_id)
    if products:
        product_obj = products.__dict__
        if product_obj['attributes']:
            attribute_string = []
            for attr in list(product_obj['attributes']):
                attribute_string.append(
                    str(get_attribute_id(str(json.loads(attr)['id']))) + 
                    " " + 
                    str(json.loads(attr)['value']).encode().decode('utf-8')
                )
            document_obj = {
                "id": product_obj['id'],
                "name": product_obj['name'],
                "description": product_obj['description'],
                "preprocessed_description":  preprocess.preprocess(product_obj['description']),
                'attribute_description': str(".".join(attribute_string))
            }
            res = es.index(index="lexical-search-index", body=document_obj)
            print(f'****res:{res}')
            init_id = init_id + 1
        else:
            init_id = init_id + 1
            time.sleep(1)
    else:
        init_id = init_id + 1
        time.sleep(1)
