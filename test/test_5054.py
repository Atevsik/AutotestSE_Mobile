from selenium.webdriver.common.by import By
import time

from pages.footballmedal import FootballOlimpMedal


def test_football_medal(browser):
    fm = FootballOlimpMedal(browser)
    fm.open()
    fm.h1()
    fm.comand(5)
    fm.sved()
    fm.h2()






