from selenium.webdriver.common.by import By
import time

from pages.nba import Nba



def test_nba(browser):
    nba = Nba(browser)
    nba.open()
    nba.h1()
    nba.dop_menu()
    nba.obsh()
















