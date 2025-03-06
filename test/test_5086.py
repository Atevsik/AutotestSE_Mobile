from selenium.webdriver.common.by import By
import time
from pages.voleyball import Voleyball


def test_volley(browser):
    volley = Voleyball(browser)
    volley.open()
    volley.h1()
    volley.dop_menu()
    volley.news()
    volley.reviews()

















