from selenium.webdriver.common.by import By
import time
from pages.lifestylemoney import LifeStyleMoney


def test_lifestyele_film(browser):
    lf_film = LifeStyleMoney(browser)
    lf_film.open()
    lf_film.h1()
    lf_film.topnews()
    lf_film.reviews()
    lf_film.hotnews()
    lf_film.expert()
    lf_film.recept()
    lf_film.h2()
    lf_film.h3()


















