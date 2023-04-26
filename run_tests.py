import os
import pytest

if __name__ == '__main__':
    test_dir = os.path.join(os.path.dirname(__file__), 'tests')
    pytest.main(['-v', test_dir])