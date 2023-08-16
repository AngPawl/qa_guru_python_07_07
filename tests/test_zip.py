import zipfile
import os.path
from os.path import basename

from .conftest import RESOURCE_ROOT_PATH


def test_successful_files_archivation():
    zip_file_path = os.path.join(RESOURCE_ROOT_PATH, 'new_zip.zip')
    with zipfile.ZipFile(zip_file_path, 'w') as new_zip:
        path_to_pdf_file = os.path.join(
            RESOURCE_ROOT_PATH, 'docs-pytest-org-en-latest.pdf'
        )

        new_zip.write(path_to_pdf_file, basename(path_to_pdf_file))

        path_to_xls_file = os.path.join(RESOURCE_ROOT_PATH, 'file_example_XLS_10.xls')

        new_zip.write(path_to_xls_file, basename(path_to_xls_file))

        path_to_xlsx_file = os.path.join(
            RESOURCE_ROOT_PATH, 'file_example_XLSX_50.xlsx'
        )

        new_zip.write(path_to_xlsx_file, basename(path_to_xlsx_file))

    files = [
        'docs-pytest-org-en-latest.pdf',
        'file_example_XLS_10.xls',
        'file_example_XLSX_50.xlsx',
    ]

    file_names = new_zip.namelist()

    assert files == file_names

    os.remove(os.path.abspath(zip_file_path))
