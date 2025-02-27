from selenium.webdriver.common.by import By
import time

from pages.eurohock import EuroHock
from pages.footballmc import FootballMc


def test_football_mc(browser):
    fm = FootballMc(browser)
    fm.open()
    fm.h1()
    fm.reklama()
    fm.book()





