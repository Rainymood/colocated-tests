import pytest

from services.adder_service import AdderService

# Ideally I would prefer to have the mock services closer to the tests, on top
# of the test files, but maybe it can be a good idea (sometimes) to have some
# global objects floating if you re-use them a lot.
@pytest.fixture()
def mock_adder_service():
    return AdderService(name="Testing Jan")
