import os
import pytest

from os_path_scripts import TESTS_PATH

if __name__ == '__main__':
	test_dir = os.path.join(TESTS_PATH)
	pytest.main(['-v', test_dir])
