from selenium.webdriver.common.by import By
import time


from pages.politika import Politika


def test_politika(browser):
    polit = Politika(browser)
    polit.open()
    polit.h1()
    polit.text()






