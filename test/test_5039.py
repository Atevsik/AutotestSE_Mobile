from selenium.webdriver.common.by import By
import time

from pages.zpkhl import zpKHL



def test_zpNHL(browser):
    zp = zpKHL(browser)
    zp.open()
    zp.h1()
    zp.filti()
    zp.input()
    zp.proverka()
    zp.player1()
    zp.player2()
    zp.select1()
    zp.select2()











