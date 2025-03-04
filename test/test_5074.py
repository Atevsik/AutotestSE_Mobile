from selenium.webdriver.common.by import By
import time

from pages.atprait import AtpRait



def test_atp_rait(browser):
   rait = AtpRait(browser)
   rait.open()
   rait.h1()
   rait.dop_menu()
   rait.obsh()















