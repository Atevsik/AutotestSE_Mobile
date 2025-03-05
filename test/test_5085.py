from selenium.webdriver.common.by import By
import time

from pages.basketeuro import Basketeuro




def test_euro_bask(browser):
    euro_b = Basketeuro(browser)
    euro_b.open()
    euro_b.h1()
    euro_b.dop_menu()
    euro_b.obsh()
















