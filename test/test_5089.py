from selenium.webdriver.common.by import By
import time

from pages.voleyballeuro4emp import VoleyballEuro4emp



def test_volley_4emp(browser):
    volley_4emp = VoleyballEuro4emp(browser)
    volley_4emp.open()
    volley_4emp.h1()
    volley_4emp.dop_menu()
    volley_4emp.news()
    volley_4emp.reviews()

















