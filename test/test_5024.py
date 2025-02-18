from selenium.webdriver.common.by import By
import time

from pages.rss import RSS




def test_reklama(browser):
    rss = RSS(browser)
    rss.open()
    rss.h1()
    rss.basket()



