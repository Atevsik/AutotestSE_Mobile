from selenium.webdriver.common.by import By
import time

from pages.biatlonmir import BiatlonMir


def test_biatlon_medal(browser):
    bitalon_mir = BiatlonMir(browser)
    bitalon_mir.open()
    bitalon_mir.h1()
    bitalon_mir.dop_menu()
    bitalon_mir.obsh()
    bitalon_mir.usa()
    bitalon_mir.m()
    bitalon_mir.j()
    bitalon_mir.s()















