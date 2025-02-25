from selenium.webdriver.common.by import By
import time

from pages.golshak import Golshak


def test_golshak(browser):
    gol = Golshak(browser)
    gol.open()
    gol.header()
    gol.reklama()
    gol.materials(16)
    gol.date()
    gol.scroll()
    gol.smi2()






