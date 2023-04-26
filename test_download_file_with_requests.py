import requests
from os_path_scripts import PROJECT_ROOT_PATH


def test_downloaded_file_with_requests():
	downloads_folder = os.path.join(PROJECT_ROOT_PATH, 'tmp')
	os.makedirs(downloads_folder, exist_ok=True)

	url = 'https://selenium.dev/images/selenium_logo_square_green.png'

	r = requests.get(url)
	file_path = os.path.join(downloads_folder, 'selenium_logo.png')
	with open(file_path, 'wb') as file:
		file.write(r.content)

	size = os.path.getsize(file_path)

	assert size == 30803
