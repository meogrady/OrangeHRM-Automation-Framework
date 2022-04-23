from pytest import fixture
from selenium import webdriver


@fixture(scope='function')
def firefox_driver():
    driver = webdriver.Firefox()
    return driver
