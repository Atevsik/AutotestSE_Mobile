from selenium.webdriver.common.by import By
import time

from pages.mmarait import MmaRait


def test_mma_rait(browser):
    rait = MmaRait(browser)
    rait.open()
    rait.h1()
    rait.boets(30)
    rait.boet()
    rait.champion()








