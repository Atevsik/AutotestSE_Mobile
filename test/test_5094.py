from selenium.webdriver.common.by import By
import time

from pages.chess import Chees


def test_chees(browser):
    chees = Chees(browser)
    chees.open()
    chees.h1()
    chees.dop_menu()
    chees.news()
    chees.reviews()

















