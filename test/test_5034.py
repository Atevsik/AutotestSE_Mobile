from selenium.webdriver.common.by import By
import time

from pages.register import Register


def test_registr(browser):
    reg = Register(browser)
    reg.open()
    reg.h1()
    reg.h2()
    reg.pole()
    reg.podval()








