import csv
import os

from os_path_scripts import PROJECT_ROOT_PATH


def test_csv():
    resources = os.path.join(PROJECT_ROOT_PATH, 'resources')
    if not os.path.exists(resources):
        os.mkdir(resources)

    csv_path = os.path.join(resources, 'eggs.csv')

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
