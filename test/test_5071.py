from selenium.webdriver.common.by import By
import time

from pages.lijimir import LijiMir


def test_lij_mir(browser):
    liji_mir = LijiMir(browser)
    liji_mir.open()
    liji_mir.h1()
    liji_mir.dop_menu()
    liji_mir.obsh()
    liji_mir.reklama()
    #liji_mir.book()
    liji_mir.gonka()
















