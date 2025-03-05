from selenium.webdriver.common.by import By
import time

from pages.shlem import Shlem




def test_shlem(browser):
   shlem = Shlem(browser)
   shlem.open()
   shlem.h1()
   shlem.dop_menu()
   shlem.obsh()















