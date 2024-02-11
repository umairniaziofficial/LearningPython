import csv

file = "find_the_link.csv"

with open(file, "r", encoding="utf-8") as file:
    csv_data = list(csv.reader(file))

diagonal_string = "".join(row[i] for i, row in enumerate(csv_data))
string2 = ""

for i, row in enumerate(csv_data):
    string2 += row[i]

print(string2)
print(diagonal_string)
