import os
import time

from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from os_path_scripts import RESOURCES_PATH


def test_download_file_with_browser():
    downloads_folder = os.path.join(RESOURCES_PATH)
    os.makedirs(downloads_folder, exist_ok=True)

    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "download.default_directory": downloads_folder,
        "download.prompt_for_download": False
    })

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    browser.config.driver = driver

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()

    time.sleep(20)

    downloaded_file = os.path.join(downloads_folder, 'pytest-main.zip')
    assert os.path.exists(downloaded_file), f"Файл не найден: {downloaded_file}"

    file_size = os.path.getsize(downloaded_file)
    expected_size = 1564394
    assert file_size == expected_size, f"Размер файла: {file_size} байт, ожидаем: {expected_size} байт"

    driver.quit()
    os.remove(downloaded_file)
