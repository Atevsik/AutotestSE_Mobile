from selenium.webdriver.common.by import By
import time

from pages.formula1 import Formula1


def test_formula(browser):
    formula = Formula1(browser)
    formula.open()
    formula.h1()
    formula.dop_menu()
    formula.obsh()
    formula.usa()















