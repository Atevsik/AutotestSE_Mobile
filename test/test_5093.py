from selenium.webdriver.common.by import By
import time


from pages.gandbollkubok import GandballKubok


def test_gandball_kubok(browser):
    gandball_kubok = GandballKubok(browser)
    gandball_kubok.open()
    gandball_kubok.h1()
    gandball_kubok.dop_menu()
    gandball_kubok.news()
    gandball_kubok.reviews()

















