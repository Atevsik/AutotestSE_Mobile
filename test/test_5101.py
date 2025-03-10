from selenium.webdriver.common.by import By
import time


from pages.lifestyle import LifeStyle


def test_lifestyele(browser):
    lf = LifeStyle(browser)
    lf.open()
    lf.h1()
    lf.topnews()
    lf.reviews()
    lf.qa()
    lf.hotnews()
    lf.expert()
    lf.recept()
    lf.h2()
    lf.h3()


















