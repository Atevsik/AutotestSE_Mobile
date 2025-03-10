from selenium.webdriver.common.by import By
import time

from pages.lifestyledeti import LifeStyleDeti



def test_lifestyele_deti(browser):
    lf_deti = LifeStyleDeti(browser)
    lf_deti.open()
    lf_deti.h1()
    lf_deti.topnews()
    lf_deti.reviews()
    lf_deti.hotnews()
    lf_deti.expert()
    lf_deti.recept()
    lf_deti.h2()
    lf_deti.h3()


















