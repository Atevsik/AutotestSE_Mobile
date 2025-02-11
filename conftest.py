import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


@pytest.fixture()
def browser():
    options = Options()
    options.page_load_strategy="eager"
    service = Service()
    #options.add_argument('--headless')
    browser = webdriver.Firefox(service=service, options=options) # options=options - в скобочках
    browser.maximize_window()
    yield browser
    browser.close()
