from selenium.webdriver.common.by import By
import time

from pages.voleyballeuro import VoleyballEuro


def test_volley_euro_euro(browser):
    volley_euro = VoleyballEuro(browser)
    volley_euro.open()
    volley_euro.h1()
    volley_euro.dop_menu()
    volley_euro.news()
    volley_euro.reviews()

















