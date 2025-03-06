from selenium.webdriver.common.by import By
import time

from pages.gandbolleuro import GandballEuro



def test_gandball_euro(browser):
    gandball_euro = GandballEuro(browser)
    gandball_euro.open()
    gandball_euro.h1()
    gandball_euro.dop_menu()
    gandball_euro.news()
    gandball_euro.reviews()

















