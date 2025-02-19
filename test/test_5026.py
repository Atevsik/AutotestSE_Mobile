from selenium.webdriver.common.by import By
import time

from pages.podpiska import Podpiska


def test_podpiska(browser):
    podpiska = Podpiska(browser)
    podpiska.open()
    podpiska.h1()
    podpiska.input()
    podpiska.knp()






