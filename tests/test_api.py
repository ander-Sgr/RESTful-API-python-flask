def test_insert_data(client):
    response = client.post('/insertdata', query_string={'data': 'test_value'})
    assert response.status_code == 201
    assert b"Value test_value created at the db" in response.data
    
def test_insert_duplicate_data(client):
    client.post('/insertdata', query_string={'data': 'test_value'})
    response = client.post('/insertdata', query_string={'data': 'test_value'})
    assert response.status_code == 409
    assert b"The value exists in the db" in response.data

def test_not_insert_nothing(client):
    response = client.post('/insertdata')
    assert response.status_code == 400
    assert b"No data provided" in response.data

def test_retrieve_all_data(client):
    response = client.post('/insertdata', query_string={'data': 'test_value'})
    response = client.post('/insertdata', query_string={'data': 'test_value2'})
    response = client.get('/getdata')
    assert response.status_code == 200
    assert b"test_value" in response.data
    assert b"test_value2" in response.data

def test_no_retrieve_nothing(client):
    response = client.get('/getdata')
    assert response.status_code == 404
    assert b"No data found" in response.data

def test_delete_data(client):
    response = client.post('/insertdata', query_string={'data': 'test_value'})
    response = client.delete('/delete', query_string={'data': 'test_value'})
    assert response.status_code == 200
    assert b"Value test_value deleted from the db" in response.data
    response = client.delete('/delete', query_string={'data': 'test_value'})

def test_no_value_provided_for_deleting(client):
    response = client.delete('/delete')
    assert response.status_code == 400
    assert b"No data provided" in response.data

def test_delete_an_inexistent_value(client):
    response = client.delete('/delete', query_string={'data': 'test_value'})
    assert response.status_code == 409
    assert b"The value not exists in the db" in response.data

def test_update_data(client):
    client.post('/insertdata', query_string={'data': 'hello world'})
    response = client.put('/update', query_string={'data': 'hello world', 'new_data': 'hello universe'})
    assert response.status_code == 200
    assert b"Value hello world updated by hello universe"

def test_update_an_inexistent_value(client):
    response = client.put('/update', query_string={'data': 'hello world', 'new_data': 'hello universe'})
    assert response.status_code == 409
    assert b"The value not exists in the db"

