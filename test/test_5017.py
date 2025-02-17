from selenium.webdriver.common.by import By
import time

from pages.stadions import Stadions


def test_stadions(browser):
    stadions = Stadions(browser)
    stadions.open()
    stadions.dopmenu()
    stadions.header()
    stadions.h1()
    stadions.h1v1()
    stadions.stadion()
    stadions.comand()
    stadions.scroll()
    stadions.smi2()