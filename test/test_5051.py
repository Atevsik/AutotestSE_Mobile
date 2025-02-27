from selenium.webdriver.common.by import By
import time

from pages.eurohock import EuroHock



def test_euro_hock(browser):
    euro_hock = EuroHock(browser)
    euro_hock.open()
    euro_hock.h1()
    euro_hock.book()
    euro_hock.scroll()
    euro_hock.smi2()


