from selenium.webdriver.common.by import By
import time
from pages.spiso4online import Spiso4Online


def test_online_spiso4(browser):
   online = Spiso4Online(browser)
   online.open()
   online.knopka()
   online.dop_news()
   online.gazeta()
   online.podpiska()
   online.k_hockey()
   online.scroll()
   online.reklama()





