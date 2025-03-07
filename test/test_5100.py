from selenium.webdriver.common.by import By
import time

from pages.fifa import FIFA


def test_fifa(browser):
    fifa = FIFA(browser)
    fifa.open()
    fifa.h1()
    fifa.news()
    fifa.reviews()

















