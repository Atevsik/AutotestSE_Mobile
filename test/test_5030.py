from selenium.webdriver.common.by import By
import time


from pages.priloj import Priloj


def test_priloj(browser):
   pril = Priloj(browser)
   pril.open()
   pril.h1()
   pril.knp()
   pril.podval()






