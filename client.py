import sys
import requests

from argparse import ArgumentParser, Namespace
from typing import List

URL = "http://127.0.0.1:8080/"

def parser_args(args: List) -> Namespace:
    parser = ArgumentParser(description="API REST")
    parser.add_argument('--insert', type=str, help="Data to insert at the db")
    parser.add_argument('--getdata', action='store_true',help="Data to delete at the db")
    return parser.parse_args(args)

def insert_data(data: str):
    params = {'data': data}
    response = requests.put(f'{URL}insert_data', params=params)
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.text}")

def get_data():
    response = requests.get(f"{URL}get_info")
    if response.ok:
        print(f"Response content: {response.text}")
    else:
        print(f"Status code: {response.status_code}")

def main(args: list):
    parsed_args = parser_args(args)
    if parsed_args.insert:
        insert_data(parsed_args.insert)
    elif  parsed_args.getdata:
        get_data()

if __name__ == "__main__":
    main(sys.argv[1:])
