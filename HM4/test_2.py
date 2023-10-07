from testpage import get, post
from conftest import get_token
import pytest
import logging

def test_step1(get_token):
    logging.info('Test 5 starting')
    result = get(get_token, {'owner': 'notMe'})
    lst = result['data']
    lst_id= [el['id'] for el in lst]
    if 82032 in lst_id:
        logging.info("SUCCESS")
    else:
        logging.error("FAIL")
    assert 82032 in lst_id
    
    
    
def test_step2(get_token):
    logging.info('Test 6 starting')
    data = {
        'title': 'test',
        'description': 'test desc2',
        'content': 'test content'
    }
    result = post(get_token, data)
    assert result
    
    result = get(get_token, {'description': data['description']})
    if result['meta']['count'] > 0:
        logging.info("SUCCESS")
    else:
        logging.error("FAIL")
    assert result['meta']['count'] > 0
    
    
if __name__ == '__main__':
    pytest.main(['-vv'])