from selenium.webdriver.common.by import By
import time

from pages.mmamc import MmaMC


def test_mma_mc(browser):
    mma_mc = MmaMC(browser)
    mma_mc.open()
    mma_mc.h1()
    mma_mc.select()
    mma_mc.bella()
    mma_mc.last()
    mma_mc.match()









