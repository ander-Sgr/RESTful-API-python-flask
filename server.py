from flask import Flask, request, Response
import csv
import os
from typing import List

app = Flask(__name__)
CSV_FILE = 'data.csv'

def create_csv_file(file_name: str=CSV_FILE) -> None:
    if not os.path.isfile(file_name):
        with open(file_name, mode="w", newline="") as file:
          csv.writer(file)


def write_data(data: str, file_name: str =CSV_FILE)-> None:
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
   lines = read_data().splitlines()
   for line in lines:
      if line == data:
         return True
   return False


def replace_data(data: str, new_data: str, file_name: str = CSV_FILE) -> None:
   lines = read_data().splitlines()
   updated_lines = []

   for line in lines:
      update_line = line.replace(data, new_data).strip()
      if update_line:
         updated_lines.append(update_line)
   with open(file_name, mode='w') as file:
      file.write("\n".join(updated_lines) + "\n")


@app.route("/insert_data", methods=['POST'])
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
   replace_data(value, "")
   return Response(f"Value {value} deleted from the db", status=200, mimetype="text/plain")


@app.route("/update", methods=['PUT'])
def update_data():
   value = request.args.get('data')
   new_value = request.args.get('new_data')
   if not value:
      return Response("No data provided", status=400, mimetype="text/plain")
   if not data_exists(value):
      return Response("The value exsits in the db", status=409, mimetype="text/plain")
   replace_data(value, new_value)
   return Response(f"Value {value} updated by {new_value}", status=200, mimetype="text/plain")

if __name__ == '__main__':
   app.run(debug=True, port=8080)
