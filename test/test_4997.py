from selenium.webdriver.common.by import By
import time
from pages.spiso4video import  Spiso4Video


def test_video_spiso4(browser):
   video = Spiso4Video(browser)
   video.open()
   video.h1()
   video.knopka()
   video.dop_news()
   video.gazeta()
   video.k_hockey()
   video.selector()
   video.mma()
   video.scroll()
   video.reklama()





