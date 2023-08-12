import csv
import os.path

# TODO оформить в тест, добавить ассерты и использовать универсальный путь


CSV_FILE_PATH = os.path.abspath('resources/new_csv.csv')
PROJECT_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(CSV_FILE_PATH)))
JOINED_PATH = os.path.join(PROJECT_ROOT_PATH, 'tests', 'resources', 'new_csv.csv')


with open(JOINED_PATH, 'w') as csv_file:
    csvwriter = csv.writer(csv_file, delimiter=';')
    csvwriter.writerow(['Bonny', 'Born', 'Peter'])
    csvwriter.writerow(['Alex', 'Serj', 'Yana'])


def test_csv_file_data():
    data = []
    with open(JOINED_PATH) as csv_file:
        csvreader = csv.reader(csv_file, delimiter=';')
        for row in csvreader:
            data.append(row)

    assert data[0] == ['Bonny', 'Born', 'Peter']
    assert data[1] == ['Alex', 'Serj', 'Yana']
