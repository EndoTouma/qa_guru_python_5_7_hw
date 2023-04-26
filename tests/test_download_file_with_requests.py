import os
import requests

from os_path_scripts import RESOURCES_PATH


def test_downloaded_file_with_requests():

	url = 'https://selenium.dev/images/selenium_logo_square_green.png'

	r = requests.get(url)
	file_path = os.path.join(RESOURCES_PATH, 'selenium_logo.png')
	with open(file_path, 'wb') as file:
		file.write(r.content)

	size = os.path.getsize(file_path)

	assert size == 30803
