from selenium.webdriver.common.by import By
import time

from pages.calendarnhl import CalendNhl



def test_nhl_calend(browser):
    nhl = CalendNhl(browser)
    nhl.open()
    nhl.h1()
    nhl.dop_menu()
    nhl.calend()
    nhl.h2()
    nhl.date()
    nhl.book()
    nhl.scroll()
    nhl.smi2()









