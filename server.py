from flask import Flask, request, jsonify, Response
import csv
import os
from typing import List

app = Flask(__name__)
CSV_FILE = 'data.csv'

def create_csv_file(file_name=CSV_FILE):
    if not os.path.isfile(file_name):
        with open(file_name, mode="w", newline="") as file:
          csv.writer(file)

def write_data(data, file_name=CSV_FILE):
   create_csv_file(file_name)
   with open(file_name, mode="a", newline="") as file:
      writer = csv.writer(file)
      writer.writerow([data])

def read_data() -> str:
   if not os.path.isfile(CSV_FILE):
      return ""
   with open(CSV_FILE, mode="r") as file:
      return file.read()
   
def data_exists(data: str) -> bool: 
   lines: List[str]

   lines = read_data().splitlines()
   for line in lines:
      if line == data:
         return True
   return False

def replace_data(data):
   s
   

@app.route("/insert_data", methods=['PUT'])
def insert_data():
   value = request.args.get('data')
   if not value:
      return Response("No data provided", status=400, mimetype="text/plain")
   if data_exists(value):
      return Response("The value exsits in the db", status=409, mimetype="text/plain")
   write_data(value)
   return Response("Value created at the db", status=201, mimetype="text/plain")


@app.route("/get_info", methods=['GET'])
def get_data():
   if read_data() == "":
      return Response("No data found", status=400, mimetype="text/plain")
   return Response(read_data(), status=200, mimetype="text/plain")


@app.route("/delete", methods=['DELETE'])
def delete_data():
   value = request.args.get('data')
   if not value:
      return Response("No data provided", status=400, mimetype="text/plain")
   if not data_exists(value):
      return Response("The value exsits in the db", status=409, mimetype="text/plain")
   lines = read_data().splitlines()

   
   
if __name__ == '__main__':
   app.run(debug=True, port=8080)
