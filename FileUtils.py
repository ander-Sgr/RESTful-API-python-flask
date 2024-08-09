import os, csv

class FileUtils:

    def __init__(self, file_name: str):
        self.file_name = file_name


    def read_data(self) -> str:
       if not os.path.isfile(self.file_name):
          return ""
       with open(self.file_name, mode="r") as file:
          return file.read()

    def create_csv_file(self) -> None:
        if not os.path.isfile(self.file_name):
            with open(self.file_name, mode="w", newline="") as file:
              file.writer(file)


    def write_data(self, data: str, file_name: str)-> None:
       self.create_csv_file(self.file_name)
       with open(file_name, mode="a", newline="") as file:
          writer = csv.writer(file)
          writer.writerow([data])


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
          updated_line = line.strip()
          if line.strip() == data:
             updated_line = new_data.strip()

          if updated_line:
             updated_lines.append(updated_line)

       with open(file_name, mode='w') as file:
          file.write("\n".join(updated_lines) + "\n")