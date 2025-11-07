import pytest
from Utils.driver_factory import create_driver # pyright: ignore[reportMissingImports]


@pytest.fixture
def setup_teardown():
    driver = create_driver()
    yield driver
    driver.quit()

