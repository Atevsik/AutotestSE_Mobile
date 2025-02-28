from selenium.webdriver.common.by import By
import time

from pages.mmamatch import MmaMatch


def test_mma_match(browser):
    match_mma = MmaMatch(browser)
    match_mma.open()
    match_mma.h1()
    match_mma.info()
    #match_mma.last_boi()
    match_mma.allnews()
    match_mma.allresult()
    match_mma.proverka(30)











