import sys, os, re
import requests

from argparse import ArgumentParser, Namespace
from typing import List

URL = "http://127.0.0.1:8080/"

def parser_args(args: List) -> Namespace:
    parser = ArgumentParser(description="API REST")
    parser.add_argument('--insert', type=str, help="Data to insert on the db")
    parser.add_argument('--getdata', action='store_true',help="Recall all the data from the db")
    parser.add_argument('--delete', type=str, help="Data to delete on the db")
    parser.add_argument('--update', action='store_true', help="action for update a value")
    parser.add_argument('--old_data', type=str, help="old data to replace")
    parser.add_argument('--new_data',type=str, help='new data for replace the old data')
    return parser.parse_args(args)
    
def insert_data(data: str):
    try:
        headers = {'Content-Type': 'text/plain'}
        data = {'data': data}
        response = requests.post(f'{URL}insertdata', params=data, headers=headers)
        response.raise_for_status()
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
    except requests.exceptions.HTTPError as http_err:
        print(http_err.response.status_code)
        print(http_err.response.text)
    except requests.exceptions.RequestException as err:
        print(f"An Error Ocurred: {err}")
        

def get_data():
    response = requests.get(f"{URL}getdata")
    if response.ok:
        print(f"Response content: {response.text}")
    elif response.status_code == 404:
        print("Resource not found\n")
        print(f"Message from the server: {response.content}")

def delete_data(data: str):
    params = {'data': data}
    response = requests.delete(f"{URL}delete", params=params)
    if response.ok:
        print(f"Response content: {response.text}")
    else:
        print(f"Response status ccode: {response.status_code}")
        print(f"Response content: {response.content}")

def update_data(data: str, new_data: str):
    params = {'data': data, 'new_data': new_data}
    response = requests.put(f"{URL}update", params=params)
    if response.ok:
        print(f"Response content: {response.content}")
    else:
        print(f"Response status ccode: {response.status_code}")
        print(f"Response content: {response.content}")

def main(args: list):
    parsed_args = parser_args(args)
    if parsed_args.insert:
        insert_data(parsed_args.insert)
    elif parsed_args.getdata:
        get_data()
    elif parsed_args.delete:
        delete_data(parsed_args.delete)
    elif parsed_args.update:
        if not parsed_args.old_data:
            print("No data provided")
        if not parsed_args.new_data:
            print("No value to update provided")
        update_data(parsed_args.old_data, parsed_args.new_data)


if __name__ == "__main__":
    main(sys.argv[1:])
