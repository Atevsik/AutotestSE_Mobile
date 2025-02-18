from selenium.webdriver.common.by import By
import time

from pages.raitingmma import MMAraiting



def test_mma_rait(browser):
    rait = MMAraiting(browser)
    rait.open()
    rait.dopmenu()
    rait.header()
    rait.h1()
    rait.h2()
    rait.h3()
    rait.boets()
    rait.champion()
    rait.jen()
    rait.vala()
