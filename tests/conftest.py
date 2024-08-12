import tempfile
import os, csv
import pytest
from server import create_app, FileUtils

@pytest.fixture
def client():
    # Crear un archivo temporal para las pruebas
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as tmp_file:
        file_name = tmp_file.name
        print(f"Temporary file created at: {file_name}")


    # Configurar la aplicación Flask con el archivo temporal
    app = create_app()
    app.config['TESTING'] = True
    app.file_utils = FileUtils(file_name)

    with app.test_client() as client:
        # Asegúrate de que el archivo CSV esté vacío al inicio
        app.file_utils.create_csv_file()
        yield client

    # Eliminar el archivo temporal después de la prueba
    os.remove(file_name)