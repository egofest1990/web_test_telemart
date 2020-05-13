import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    browser: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    yield browser
    browser.quit()