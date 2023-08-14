import xlrd
import os.path

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

XLS_FILE_PATH = os.path.abspath('resources/file_example_XLS_10.xls')
PROJECT_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(XLS_FILE_PATH)))
JOINED_PATH = os.path.join(
    PROJECT_ROOT_PATH, 'tests', 'resources', 'file_example_XLS_10.xls'
)


def test_number_of_sheets():
    book = xlrd.open_workbook('resources/file_example_XLS_10.xls')

    expected_nsheets = 1

    assert book.nsheets == expected_nsheets


def test_names_of_sheets():
    book = xlrd.open_workbook('resources/file_example_XLS_10.xls')

    expected_sheet_name = ['Sheet1']

    assert book.sheet_names() == expected_sheet_name


def test_number_of_columns():
    book = xlrd.open_workbook('resources/file_example_XLS_10.xls')

    sheet = book.sheet_by_index(0)

    expected_ncols = 8

    assert sheet.ncols == expected_ncols


def test_number_of_rows():
    book = xlrd.open_workbook('resources/file_example_XLS_10.xls')

    sheet = book.sheet_by_index(0)

    expected_nrows = 10

    assert sheet.nrows == expected_nrows


def test_column_cross_row_cell_value():
    book = xlrd.open_workbook('resources/file_example_XLS_10.xls')

    sheet = book.sheet_by_index(0)

    row = 3
    col = 2

    assert sheet.cell_value(rowx=row, colx=col) == 'Gent'


def test_value_of_rows():
    book = xlrd.open_workbook('resources/file_example_XLS_10.xls')

    expected_values = [
        [0.0, 'First Name', 'Last Name', 'Gender', 'Country', 'Age', 'Date', 'Id'],
        [1.0, 'Dulce', 'Abril', 'Female', 'United States', 32.0, '15/10/2017', 1562.0],
        [
            2.0,
            'Mara',
            'Hashimoto',
            'Female',
            'Great Britain',
            25.0,
            '16/08/2016',
            1582.0,
        ],
        [3.0, 'Philip', 'Gent', 'Male', 'France', 36.0, '21/05/2015', 2587.0],
        [
            4.0,
            'Kathleen',
            'Hanner',
            'Female',
            'United States',
            25.0,
            '15/10/2017',
            3549.0,
        ],
        [
            5.0,
            'Nereida',
            'Magwood',
            'Female',
            'United States',
            58.0,
            '16/08/2016',
            2468.0,
        ],
        [6.0, 'Gaston', 'Brumm', 'Male', 'United States', 24.0, '21/05/2015', 2554.0],
        [7.0, 'Etta', 'Hurn', 'Female', 'Great Britain', 56.0, '15/10/2017', 3598.0],
        [
            8.0,
            'Earlean',
            'Melgar',
            'Female',
            'United States',
            27.0,
            '16/08/2016',
            2456.0,
        ],
        [
            9.0,
            'Vincenza',
            'Weiland',
            'Female',
            'United States',
            40.0,
            '21/05/2015',
            6548.0,
        ],
    ]

    sheet = book.sheet_by_index(0)

    for i in range(sheet.nrows):
        assert sheet.row_values(i) == expected_values[i]
