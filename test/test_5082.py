from selenium.webdriver.common.by import By
import time

from pages.trassa import FormulaTrassa


def test_f_trassa(browser):
    f_trassa = FormulaTrassa(browser)
    f_trassa.open()
    f_trassa.h1()
    f_trassa.text()
    f_trassa.dop_menu()
    f_trassa.obsh()

















