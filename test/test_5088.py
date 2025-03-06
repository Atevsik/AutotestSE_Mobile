from selenium.webdriver.common.by import By
import time

from pages.voleyballworld import VoleyballWorld


def test_volley_world(browser):
    volley_world = VoleyballWorld(browser)
    volley_world.open()
    volley_world.h1()
    volley_world.dop_menu()
    volley_world.news()
    volley_world.reviews()

















