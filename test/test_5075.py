from selenium.webdriver.common.by import By
import time

from pages.wta import Wta



def test_wta(browser):
   wta = Wta(browser)
   wta.open()
   wta.h1()
   wta.dop_menu()
   wta.obsh()















