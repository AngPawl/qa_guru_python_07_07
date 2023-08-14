import pypdf
import os.path

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

PDF_FILE_PATH = os.path.abspath('resources/docs-pytest-org-en-latest.pdf')
PROJECT_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(PDF_FILE_PATH)))
JOINED_PATH = os.path.join(
    PROJECT_ROOT_PATH, 'tests', 'resources', 'docs-pytest-org-en-latest.pdf'
)


def test_number_of_pages():
    with open(JOINED_PATH, 'rb') as pdf_file:
        reader = pypdf.PdfReader(pdf_file)

        number_of_pages = len(reader.pages)

        print(number_of_pages)

        assert number_of_pages == 412


def test_first_page_text():
    with open(JOINED_PATH, 'rb') as pdf_file:
        reader = pypdf.PdfReader(pdf_file)

        first_page = reader.pages[0]

        text = first_page.extract_text()

        assert (
            text
            == "pytest Documentation\nRelease 0.1\nholger krekel, trainer and consultant, https://merlinux.eu/\nJul 14, 2022"
        )


def test_number_of_images_on_first_page():
    with open(JOINED_PATH, 'rb') as pdf_file:
        reader = pypdf.PdfReader(pdf_file)
        first_page = reader.pages[0]
        count = 0
        for image_file in first_page.images:
            with open(str(count) + image_file.name, 'wb') as fp:
                fp.write(image_file.data)
                count += 1

    assert count == 1
