from selenium.webdriver.common.by import By
import time

from pages.melbet import Melbet
from pages.mmakalend import MmaCalend


def test_mma_calend(browser):
    mma = MmaCalend(browser)
    mma.open()
    mma.h1()
    mma.filters()
    mma.book()
    mma.match()
    mma.select()
    mma.aca()







