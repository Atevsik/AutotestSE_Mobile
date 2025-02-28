from selenium.webdriver.common.by import By
import time

from pages.matchpagemma import MmaMatchPage


def test_mma_match_page(browser):
    page = MmaMatchPage(browser)
    page.open()
    page.h1()
    page.books()
    page.vs()
    page.shon()
    page.vera()
    page.stat()












