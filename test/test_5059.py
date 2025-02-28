from selenium.webdriver.common.by import By
import time

from pages.mmaboets import MmaBoets



def test_mma_boets(browser):
    boets = MmaBoets(browser)
    boets.open()
    boets.h1()
    boets.player()
    boets.women()









