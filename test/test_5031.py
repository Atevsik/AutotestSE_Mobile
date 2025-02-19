from selenium.webdriver.common.by import By
import time

from pages.podpis import Podpis


def test_priloj(browser):
    podpis = Podpis(browser)
    podpis.open()
    podpis.h1()
    podpis.gazeta1()
    podpis.oformit()
    podpis.knp()





