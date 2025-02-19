from selenium.webdriver.common.by import By
import time

from pages.brend import Brend



def test_brend(browser):
    brend = Brend(browser)
    brend.open()
    brend.h1()
    brend.knp(2)
    brend.h2()






