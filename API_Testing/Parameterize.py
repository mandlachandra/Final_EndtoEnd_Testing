import pytest

import requests

@pytest.mark.parametrize("user_id",[1,2,3])
def test_get_call(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{user_id}")
    assert response.status_code == 200




