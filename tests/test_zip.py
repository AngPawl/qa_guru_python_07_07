import zipfile
import os.path
from os.path import basename

from .conftest import RESOURCE_ROOT_PATH


def test_successful_files_archivation():
    zip_file_path = os.path.join(RESOURCE_ROOT_PATH, 'new_zip.zip')

    files = [
        'docs-pytest-org-en-latest.pdf',
        'file_example_XLS_10.xls',
        'file_example_XLSX_50.xlsx',
    ]

    with zipfile.ZipFile(zip_file_path, 'w') as new_zip:
        for file in files:
            path_to_file = os.path.join(RESOURCE_ROOT_PATH, file)

            new_zip.write(path_to_file, basename(path_to_file))

    file_names = new_zip.namelist()

    assert files == file_names

    os.remove(os.path.abspath(zip_file_path))
