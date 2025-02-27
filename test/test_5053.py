from selenium.webdriver.common.by import By
import time

from pages.footballolimp import FootballOlimp


def test_football_olimp(browser):
    fo = FootballOlimp(browser)
    fo.open()
    fo.h1()
    fo.fot()
    fo.men()






