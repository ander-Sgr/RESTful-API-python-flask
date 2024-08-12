import pytest
import tempfile
import os
from server import create_app
from FileUtils import FileUtils

@pytest.fixture
def client():
    # Crear un archivo temporal para las pruebas
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as tmp_file:
        file_name = tmp_file.name

    # Configurar la aplicación para usar el archivo temporal
    app = create_app()
    app.config['TESTING'] = True# Configurar el archivo CSV temporal
    app.file_utils = FileUtils(file_name)  # Inicializar FileUtils
    try:
        with app.test_client() as client:
            yield client
    finally:
        os.remove(file_name)

    print(file_name)
