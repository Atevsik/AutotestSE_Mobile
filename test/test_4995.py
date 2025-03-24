from selenium.webdriver.common.by import By
import time
from pages.spiso4news import NewsSpiso4


def test_news_spiso4(browser):
    news = NewsSpiso4(browser)
    news.open()
    news.h1()
    news.knopka()
    news.knopki1()
    news.knopki2()
    news.knopki3()
    #news.vid_sport()
    #news.dop_news()        #Здесь мешает банер, во второй версии исправить это, сделать проверку если он есть, закрывать
    news.k_football()
    #news.proverka(20)
    news.selector()
    news.rpl()
    news.scroll()
    news.reklama()





