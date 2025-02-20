from selenium.webdriver.common.by import By
import time


from pages.poisk import Poisk


def test_poisk(browser):
    poisk = Poisk(browser)
    poisk.open()
    poisk.menu()
    poisk.input()
    poisk.h1()
    poisk.text(30)
    poisk.next_page()
    poisk.scroll()
    poisk.smi2()






