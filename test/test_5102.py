from selenium.webdriver.common.by import By
import time



from pages.lifestylemed import LifeStyleMed


def test_lifestyele_med(browser):
    lf_med = LifeStyleMed(browser)
    lf_med.open()
    lf_med.h1()
    lf_med.topnews()
    lf_med.reviews()
    lf_med.qa()
    lf_med.hotnews()
    lf_med.expert()
    lf_med.recept()
    lf_med.h2()
    lf_med.h3()


















