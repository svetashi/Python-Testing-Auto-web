from rest_api import get
from fixtures import get_token
import pytest

def test_step1(get_token):
    result = get(get_token, {'owner': 'notMe'})
    lst = result['data']
    lst_id= [el['id'] for el in lst]
    assert 80485 in lst_id
    
    
if __name__ == '__main__':
    pytest.main(['-vv'])