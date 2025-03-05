from selenium.webdriver.common.by import By
import time

from pages.basket import Basket



def test_basket(browser):
    basket = Basket(browser)
    basket.open()
    basket.h1()
    basket.dop_menu()
    basket.obsh()
















