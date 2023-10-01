from rest_api import post, get
from fixtures import get_token
import pytest

def test_step2(get_token):
    data = {
        'title': 'test',
        'description': 'test desc2',
        'content': 'test content'
    }
    result = post(get_token, data)
    assert result
    
    result = get(get_token, {'description': data['description']})
    assert result['meta']['count'] > 0
    
if __name__ == '__main__':
    pytest.main(['-vv'])