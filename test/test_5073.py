from selenium.webdriver.common.by import By
import time

from pages.lijirussia import LijiRussia


def test_lij_russia(browser):
    lij_rus = LijiRussia(browser)
    lij_rus.open()
    lij_rus.h1()
    lij_rus.dop_menu()
    lij_rus.obsh()















