from selenium.webdriver.common.by import By
import time

from pages.matchpagehockey import MatchHock


def test_match_hock(browser):
    mh = MatchHock(browser)
    mh.open()
    # переписать это дерьмо


















