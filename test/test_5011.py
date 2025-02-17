from selenium.webdriver.common.by import By
import time

from pages.mc import MC




def test_mc(browser):
    mc = MC(browser)
    mc.open()
    mc.h1()
    mc.dopmenu()
    mc.reklama()
    mc.header()
    mc.knopi()
    mc.h2()
    mc.sport_navigator()
    mc.scroll()
    mc.smi2()