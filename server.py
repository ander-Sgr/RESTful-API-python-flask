from flask import Flask, request, Response
import csv
import os
from typing import List
from FileUtils import *

app = Flask(__name__)
CSV_FILE = 'data.csv'
file_utils = FileUtils(CSV_FILE)

@app.route("/insert_data", methods=['POST'])
def insert_data():
   value = request.args.get('data')
   if not value:
      return Response("No data provided", status=400, mimetype="text/plain")
   if file_utils.data_exists(value):
      return Response("The value exsits in the db", status=409, mimetype="text/plain")
   file_utils.write_data(value)
   return Response("Value created at the db", status=201, mimetype="text/plain")


@app.route("/get_info", methods=['GET'])
def get_data():
   if file_utils.read_data() == "":
      return Response("No data found", status=400, mimetype="text/plain")
   return Response(file_utils.read_data(), status=200, mimetype="text/plain")


@app.route("/delete", methods=['DELETE'])
def delete_data():
   value = request.args.get('data')
   if not value:
      return Response("No data provided", status=400, mimetype="text/plain")
   if not file_utils.data_exists(value):
      return Response("The value not exsits in the db", status=409, mimetype="text/plain")
   file_utils.replace_data(value, "")
   return Response(f"Value {value} deleted from the db", status=200, mimetype="text/plain")


@app.route("/update", methods=['PUT'])
def update_data():
   value = request.args.get('data')
   new_value = request.args.get('new_data')
   if not value:
      return Response("No data provided", status=400, mimetype="text/plain")
   if not file_utils.data_exists(value):
      return Response("The value to replace not exsits in the db", status=409, mimetype="text/plain")
   elif file_utils.data_exists(new_value):
      return Response("The new value exists in the db")
   file_utils.replace_data(value, new_value)
   return Response(f"Value {value} updated by {new_value}", status=200, mimetype="text/plain")

if __name__ == '__main__':
   app.run(debug=True, port=8080)
