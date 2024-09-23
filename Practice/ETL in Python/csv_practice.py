import csv

# Reader
with open("Practice/ETL in Python/file.csv", newline="", encoding="utf8") as csv_file:
    csv_data = csv.reader(csv_file)
    for row in csv_data:
        print(row)

# Writer
with open("Practice/ETL in Python/new.csv", mode="a", newline="", encoding="utf8") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")
    data = ['5', 'Lawrence', '2000']
    csv_writer.writerow(data)