from selenium.webdriver.common.by import By
import time

from pages.cs import Cs


def test_dota(browser):
    dota = Cs(browser)
    dota.open()
    dota.h1()
    dota.news()
    dota.reviews()

















