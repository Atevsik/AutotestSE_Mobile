from selenium.webdriver.common.by import By
import time

from pages.hockey24 import Hock24



def test_hock24(browser):
    hoc24 = Hock24(browser)
    hoc24.open()
    hoc24.h1()
    hoc24.dop_menu()
    hoc24.comand()
    hoc24.h2()
    hoc24.spisok(10)
    hoc24.sostav()
    hoc24.calend()
    #hoc24.stat()














