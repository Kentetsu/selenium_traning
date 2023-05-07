import pytest
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


DRIVERS_STORAGE = "/home/kentetsu/Документы/webDrivers/"


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="Browser to run tests"
    ),
    parser.addoption(
        "--url", default="http://localhost:8081", help="URL to run tests"
    ),
    parser.addoption(
        "--wait"
    )


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")
    _driver = None
    if browser_name == "chrome":
        S = Service(f'{DRIVERS_STORAGE}/chromedriver')
        capa = DesiredCapabilities.CHROME
        capa["pageLoadStrategy"] = "none"
        _driver = webdriver.Chrome(service=S, desired_capabilities=capa)

    elif browser_name == "firefox":
        S = Service(f'{DRIVERS_STORAGE}/geckodriver')
        capa = DesiredCapabilities.FIREFOX
        capa["pageLoadStrategy"] = "none"
        _driver = webdriver.Firefox(service=S, desired_capabilities=capa)
    elif browser_name == "opera":
        S = Service(f'{DRIVERS_STORAGE}/operadriver')
        _driver = webdriver.Chrome(service=S)
    elif browser_name == "edge":
        S = Service(f'{DRIVERS_STORAGE}/msedgedriver')
        capa = DesiredCapabilities.EDGE
        capa["pageLoadStrategy"] = "none"
        _driver = webdriver.ChromiumEdge(service=S)

    yield _driver
    _driver.close()


@pytest.fixture()
def url(request):
    url = request.config.getoption("--url")
    return url


@pytest.fixture()
def wait():
    wait = WebDriverWait(driver, 5, poll_frequency=1)
    return wait
