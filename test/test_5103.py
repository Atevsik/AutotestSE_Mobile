from selenium.webdriver.common.by import By
import time




from pages.lifestyletren import LifeStyleMedTren


def test_lifestyele_tren(browser):
    lf_tren = LifeStyleMedTren(browser)
    lf_tren.open()
    lf_tren.h1()
    lf_tren.topnews()
    lf_tren.reviews()
    lf_tren.qa()
    lf_tren.hotnews()
    lf_tren.expert()
    lf_tren.recept()
    lf_tren.h2()
    lf_tren.h3()


















