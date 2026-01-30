import pytest
from selenium import webdriver


@pytest.fixture
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture
def setupBigB(request):
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture
def setupBookMovies(request):
    driver = webdriver.Chrome()
    driver.get("https://in.bookmyshow.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
