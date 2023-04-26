import os
import xlrd

from os_path_scripts import RESOURCES_PATH


def test_xls():
    excel_path = os.path.join(RESOURCES_PATH, 'file_example_XLS_10.xls')

    book = xlrd.open_workbook(excel_path)
    print(f'Количество листов {book.nsheets}')
    print(f'Имена листов {book.sheet_names()}')
    sheet = book.sheet_by_index(0)
    print(f'Количество столбцов {sheet.ncols}')
    print(f'Количество строк {sheet.nrows}')
    print(f'Пересечение строки 9 и столбца 1 = {sheet.cell_value(rowx=9, colx=1)}')
    # печать всех строк по очереди
    for rx in range(sheet.nrows):
        print(sheet.row(rx))

    assert book.nsheets == 1
    assert book.sheet_names()[0] == 'Sheet1'
    assert sheet.ncols == 8
    assert sheet.nrows == 10
    assert sheet.cell_value(rowx=9, colx=1) == 'Vincenza'

