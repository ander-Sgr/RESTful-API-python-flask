def test_insert_data(client):
    # Primera inserción del dato
    data = {'data': 'hello'}
    response = client.post('/insertdata', query_string=data)
    
    # Verifica que la primera inserción fue exitosa (201 Created)
    assert response.status_code == 201, f"Expected 201, but got {response.status_code}"
    assert b"Value hello created at the db" in response.data
    
