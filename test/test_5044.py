from selenium.webdriver.common.by import By
import time
from pages.khl import KHL


def test_khl(browser):
    khl = KHL(browser)
    khl.open()
    khl.h1()
    khl.dop_menu()
    khl.table()
    khl.h2()
    khl.konf1()
    khl.konf2()
    khl.so4()
    khl.konferen()
    khl.vost()
    khl.zap()
    khl.scroll()
    khl.smi2()
    khl.obsh()
    khl.regulr()









