from selenium.webdriver.common.by import By
import time

from pages.bill import Bill



def test_wta(browser):
   wta = Bill(browser)
   wta.open()
   wta.h1()
   wta.dop_menu()
   wta.obsh()















