import os
from openpyxl import load_workbook


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

XLSX_FILE_PATH = os.path.abspath('resources/file_example_XLSX_50.xlsx')
PROJECT_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(XLSX_FILE_PATH)))
JOINED_PATH = os.path.join(
    PROJECT_ROOT_PATH, 'tests', 'resources', 'file_example_XLSX_50.xlsx'
)


def test_cell_value():
    workbook = load_workbook('resources/file_example_XLSX_50.xlsx')
    sheet = workbook.active

    row = 3
    col = 2

    expected_value = 'Mara'

    assert sheet.cell(row=row, column=col).value == expected_value
