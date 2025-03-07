from selenium.webdriver.common.by import By
import time

from pages.lol import LOL


def test_lol(browser):
    lol = LOL(browser)
    lol.open()
    lol.h1()
    lol.news()
    lol.reviews()

















