from selenium.webdriver.common.by import By
import time

from pages.detalonline import DetalOnline



def test_detal_online(browser):
    detal_online = DetalOnline(browser)
    detal_online.open()
    detal_online.header()
    detal_online.podelit()
    detal_online.podel_knop(5)
    detal_online.footer()
    detal_online.teg()
    detal_online.date_online()

