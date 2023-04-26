import os
import zipfile

from os_path_scripts import PROJECT_ROOT_PATH


def test_zip_files():
    resources = os.path.join(PROJECT_ROOT_PATH, 'resources')
    file_names = os.listdir(resources)
    archive_name = os.path.join(resources, 'test.zip')

    with zipfile.ZipFile(archive_name, mode='w', compression=zipfile.ZIP_DEFLATED) as archive:
        for file_name in file_names:
            file_path = os.path.join(resources, file_name)
            archive.write(file_path, file_name)

    with zipfile.ZipFile(archive_name, mode='r') as archive:
        expected_files = ['docs-pytest-org-en-latest.pdf', 'eggs.csv', 'file_example_XLSX_50.xlsx', 'file_example_XLS_10.xls', 'selenium_logo.png']
        actual_files = archive.namelist()
        assert set(expected_files) == set(actual_files), f"Unexpected archive contents: {actual_files}"

