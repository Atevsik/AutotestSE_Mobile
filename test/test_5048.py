from selenium.webdriver.common.by import By
import time

from pages.khltreners import Treners


def test_khl_treners(browser):
    treners = Treners(browser)
    treners.open()
    treners.h1()
    treners.text()
    treners.mixa()
    treners.spisok(20)
    treners.knop()
    treners.spisok(32)
    treners.scroll()
    treners.smi2()














