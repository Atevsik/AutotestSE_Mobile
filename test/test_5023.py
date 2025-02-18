from selenium.webdriver.common.by import By
import time

from pages.reklama import Reklama




def test_reklama(browser):
    rekl = Reklama(browser)
    rekl.open()
    rekl.h1()
    rekl.ever()
    rekl.name1()
    rekl.tell1()
    rekl.name2()
    rekl.tel2()
    rekl.name3()
    rekl.tel3()


