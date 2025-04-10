from selenium.webdriver.common.by import By
import time

from pages.detalnews import DetalNews



def test_detal_news(browser):
    detal_news = DetalNews(browser)
    detal_news.open()
    detal_news.tablo()
    detal_news.knopki()
    detal_news.autor()
    detal_news.podelit()
    detal_news.podel_knop(5)
    detal_news.reklama()
    detal_news.detal_menu()
    detal_news.telega_news()
    detal_news.header()
    #gdetal_news.basket()
    detal_news.block_next()
    detal_news.like()







