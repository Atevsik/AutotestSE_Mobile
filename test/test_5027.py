from selenium.webdriver.common.by import By
import time

from pages.contact import Contakt
from pages.podpiska import Podpiska


def test_contakt(browser):
    cont = Contakt(browser)
    cont.open()
    cont.h1()
    cont.h2()
    cont.h3()
    cont.h4()






