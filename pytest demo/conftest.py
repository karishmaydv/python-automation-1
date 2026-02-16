import pytest

#The yield statement in a fixture is used to separate setup and teardown logic.

@pytest.fixture(scope="class")
def setup():
    print("i will be exectuing first")
    yield
    print("i will be execute last")

def dataload():
    print("user profile data is being created")
    return ("karishma","yadav", "karishmaydv05@gmail.com")

