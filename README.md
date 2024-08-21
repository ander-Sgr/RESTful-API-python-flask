# SPRINT04 - LAB03

## Requistos

- python >= 3.11
- pip >= 21.2.1

## Instalación

Creamos nuestro virtual env

```bash
python3 -m venv .venv
source  .venv/bin/activate
```

Intalamos los requirements

```bash
pip install -r requirements.txt
```

## Pasos para ejecutar la aplicación

Primero ejecutamos nuestro servidor que es donde tenemos definos nuestros metodos CRUD

```bash
 python server.py 
```

El cliente recibe los siguientes argumentos

- `--insert`: Insertar datos a la DB
- `--getdata`: Recupera todos los datos de la DB.
- `--delete`: Borra datos la DB.
- `--update`: Actualiza datos de la DB
- `--old_data`: Dato acutal en la DB.
- `--new_data`: Nuevo dato para la DB.

### Usos del cliente

Hay que tener corriendo el servidor.

Para obtener todos los datos de la db.

```bash
python client.py --getdata
```

En caso de no haber ningun fichero el servidor nos devolverá:

```text
Resource not found
```

Para poder insertar un nuevo dato a la DB

```bash
python client.py --insert <data a insertar>
```

En caso de que el fichero no exista, lo que hará el servidor es crearlo e
insertará el dato indicado en el parametro.

Borrar un dato del fichero

```bash
python client.py --delete <data a borrar>
```

Actualizar un dato existente en la DB.

```bash
python client.py --update  --old_data <data antiguo> --new_data <nuevo data>
```
