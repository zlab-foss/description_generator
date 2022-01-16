import requests
import json

def get_token():
        login_obj = requests.post(
            f"https://api.shahreketabonline.com/Login",
            json={
                "email": "zlab@fanap.ir",
                "password": "ZL@b$1399"
            }
        )
        return login_obj.json()



def get_attribute_id(attribute_id: str):
    attributes_list = requests.get(
        f"https://api.shahreketabonline.com/SemanticSearch/GetAttributes",
        headers={'Authorization': f'Bearer {get_token()["accessToken"]}'}
    )
    for val in json.loads(attributes_list.__dict__['_content']):
        if str(val['id']) == attribute_id:
            return val['title']
