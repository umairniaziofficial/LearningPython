import csv
import os

os.system("cls")
data = open("example.csv", encoding="utf-8")

csv_data = csv.reader(data)

data_lines = list(csv_data)

file_to_output = open("to_save_file.csv", mode="w", newline="")

csv_writer = csv.writer(file_to_output, delimiter=",")

csv_writer.writerow(["a", "b", "c"])

csv_writer.writerows([[1, 2, 3], [4, 5, 6]])

file_to_output.close()
data.close()
