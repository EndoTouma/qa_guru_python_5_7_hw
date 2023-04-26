import os
from pypdf import PdfReader

from os_path_scripts import RESOURCES_PATH


def test_pdf():
	pdf_path = os.path.join(RESOURCES_PATH, 'docs-pytest-org-en-latest.pdf')
	with open(pdf_path, 'rb') as file:
		reader = PdfReader(file)
		number_of_pages = len(reader.pages)
		page = reader.pages[0]
		text = page.extract_text()
		print(page)
		print(number_of_pages)
		print(text)
		assert number_of_pages == 412
		assert text == 'pytest Documentation\n' \
		               'Release 0.1\n' \
		               'holger krekel, trainer and consultant, https://merlinux.eu/\n' \
		               'Jul 14, 2022'
