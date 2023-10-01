import requests
import yaml
import json

with open('config.yaml', 'r') as f:
    conf =  yaml.safe_load(f)
    

def get_token():
    response = requests.post(url=conf['url'], data={'username': conf['username'], 'password': conf['password']})
    return response.json()['token']

def get(token: str, params: dict):
    response = requests.get(conf['url_post'], headers={'X-Auth-Token': token}, params=params)
    return response.json()

def post(token: str, data: dict):
    response = requests.post(conf['url_post'], headers={'X-Auth-Token': token}, data=data)
    return response.json()


if __name__ == '__main__':
    temp = get_token()
    print(get(temp))