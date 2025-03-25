from selenium.webdriver.common.by import By
import time

from pages.devis import Devis



# Иногда валится, запустить если что повторно
def test_devis(browser):
   devis = Devis(browser)
   devis.open()
   devis.h1()
   devis.dop_menu()
   devis.obsh()















