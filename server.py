from flask import Flask, request, Response
import csv
import os
from typing import List
from FileUtils import *

CSV_FILE = 'data.csv'

def create_app(file_utils=None):
   app = Flask(__name__)
   app.file_utils = file_utils or FileUtils(CSV_FILE)
   
   @app.route("/insertdata", methods=['POST'])
   def insert_data():
      try:
         value = request.args.get('data')
         if not value:
            return Response("No data provided", status=400, mimetype="text/plain")
         if app.file_utils.data_exists(value):
            return Response("The value exists in the db", status=409, mimetype="text/plain")
         app.file_utils.write_data(value)
         return Response(f"Value {value} created at the db", status=201, mimetype="text/plain")
      except Exception as e:
         return Response(f"An error ocurred: {str(e)}", status=500, mimetype="text/plain")


   @app.route("/getdata", methods=['GET'])
   def get_data():
      try:
         data = app.file_utils.read_data()
         if not data:
            return Response("No data found", status=404, mimetype="text/plain")
         return Response(data, status=200, mimetype="text/plain")
      except Exception as e:
         return Response(f"An error ocurred: {str(e)}", status=500, mimetype="text//plain")

   @app.route("/delete", methods=['DELETE'])
   def delete_data():
      value = request.args.get('data')
      if not value:
         return Response("No data provided", status=400, mimetype="text/plain")
      if not app.file_utils.data_exists(value):
         return Response("The value not exists in the db", status=409, mimetype="text/plain")
      app.file_utils.replace_data(value, "")
      return Response(f"Value {value} deleted from the db", status=200, mimetype="text/plain")


   @app.route("/update", methods=['PUT'])
   def update_data():
      value = request.args.get('data')
      new_value = request.args.get('new_data')
      if not value:
         return Response("No data provided", status=400, mimetype="text/plain")
      if not app.file_utils.data_exists(value):
         return Response("The value to replace not exsits in the db", status=409, mimetype="text/plain")
      elif app.file_utils.data_exists(new_value):
         return Response("The new value exists in the db")
      app.file_utils.replace_data(value, new_value)
      return Response(f"Value {value} updated by {new_value}", status=200, mimetype="text/plain")
   return app

if __name__ == '__main__':
   app = create_app()
   app.run(debug=True, port=8080)