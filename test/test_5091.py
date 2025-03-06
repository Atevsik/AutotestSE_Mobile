from selenium.webdriver.common.by import By
import time




from pages.gandbollmir import GandballMir


def test_gandball_mir(browser):
    gandball_mir = GandballMir(browser)
    gandball_mir.open()
    gandball_mir.h1()
    gandball_mir.dop_menu()
    gandball_mir.news()
    gandball_mir.reviews()

















