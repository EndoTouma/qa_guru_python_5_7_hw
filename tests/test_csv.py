import csv
import os

from os_path_scripts import RESOURCES_PATH


def test_csv():
    csv_path = os.path.join(RESOURCES_PATH, 'eggs.csv')

    with open(csv_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    read_data = []
    with open(csv_path, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            read_data.append(row)

    assert read_data == [['Anna', 'Pavel', 'Peter'], ['Alex', 'Serj', 'Yana']], f"Unexpected CSV data: {read_data}"
