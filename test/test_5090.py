from selenium.webdriver.common.by import By
import time

from pages.gandboll import Gandball




def test_gandball(browser):
    gandball = Gandball(browser)
    gandball.open()
    gandball.h1()
    gandball.dop_menu()
    gandball.news()
    gandball.reviews()

















