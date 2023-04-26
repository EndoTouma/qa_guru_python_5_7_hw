import os

CURRENT_FILE_PATH = os.path.abspath(__file__)

PROJECT_ROOT_PATH = os.path.dirname(CURRENT_FILE_PATH)

RESOURCES_PATH = os.path.join(PROJECT_ROOT_PATH, 'resources', )

TESTS_PATH = os.path.join(PROJECT_ROOT_PATH, 'tests')