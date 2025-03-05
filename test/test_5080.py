from selenium.webdriver.common.by import By
import time

from pages.fkalend import FormulaCalend



def test_f_calend_calend(browser):
    f_calend = FormulaCalend(browser)
    f_calend.open()
    f_calend.h1()
    f_calend.dop_menu()
    f_calend.obsh()
    f_calend.vibor()
    f_calend.reklama()
    f_calend.redbull()
    f_calend.serxio()
















