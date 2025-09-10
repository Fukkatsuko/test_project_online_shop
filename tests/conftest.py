import pytest

@pytest.fixture(scope="module")
def set_group():
    print("\nStart all tests")
    yield
    print("\nFinish all tests")