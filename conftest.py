import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


@pytest.fixture()
def browser():
    options = Options()
    options.page_load_strategy="eager"
    options.set_preference("general.useragent.override",
                           "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36")
    service = Service()
    #options.add_argument('--headless')
    browser = webdriver.Firefox(service=service, options=options) # options=options - в скобочках
    browser.set_window_size(375, 812)
    yield browser
    browser.close()
