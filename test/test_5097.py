from selenium.webdriver.common.by import By
import time

from pages.dota import Dota


def test_dota(browser):
    dota = Dota(browser)
    dota.open()
    dota.h1()
    dota.news()
    dota.btn()
    dota.reviews()

















