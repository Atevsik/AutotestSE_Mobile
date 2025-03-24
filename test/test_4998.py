from selenium.webdriver.common.by import By
import time

from pages.spiso4photo import Spiso4Photo


def test_photo_spiso4(browser):
   photo = Spiso4Photo(browser)
   photo.open()
   photo.h1()
   photo.knopka()
   photo.dop_news()
   photo.gazeta()
   photo.k_hockey()
   photo.selector()
   photo.mma()
   photo.scroll()
   photo.reklama()





