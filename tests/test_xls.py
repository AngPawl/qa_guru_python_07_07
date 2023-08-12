import xlrd
# TODO оформить в тест, добавить ассерты и использовать универсальный путь

book = xlrd.open_workbook('resources/file_example_XLS_10.xls')

print(f'Количество листов {book.nsheets}')
print(f'Имена листов {book.sheet_names()}')
sheet = book.sheet_by_index(0)
print(f'Количество колонок  {sheet.ncols}')
print(f'Количество строк    {sheet.nrows}')
print(f'Пересечение строки и столбца {sheet.cell_value(rowx=3, colx=2)}')
for rx in range(sheet.nrows):
    print(sheet.row(rx))