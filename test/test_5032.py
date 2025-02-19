from selenium.webdriver.common.by import By
import time

from pages.fact import Ffct


def test_priloj(browser):
    fact = Ffct(browser)
    fact.open()
    fact.h1()
    fact.text()





