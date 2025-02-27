from selenium.webdriver.common.by import By
import time

from pages.melbet import Melbet


def test_melbet(browser):
    mel = Melbet(browser)
    mel.open()
    mel.h1()
    mel.knopki1()
    mel.knopki2()
    mel.knopki3()
    mel.material(10)







