# Import the csv and os modules
import csv
import os

# Clear the console screen
os.system("cls")

# Open the CSV file in read mode with specified encoding
data = open("example.csv", encoding="utf-8")

# Create a CSV reader object
csv_data = csv.reader(data)

# Convert the CSV data to a list
data_lines = list(csv_data)

# Open a new CSV file in write mode
file_to_output = open("to_save_file.csv", mode="w", newline="")

# Create a CSV writer object with specified delimiter
csv_writer = csv.writer(file_to_output, delimiter=",")

# Write a header row to the new CSV file
csv_writer.writerow(["a", "b", "c"])

# Write multiple rows to the new CSV file
csv_writer.writerows([[1, 2, 3], [4, 5, 6]])

# Close the new CSV file
file_to_output.close()

# Close the original CSV file
data.close()
