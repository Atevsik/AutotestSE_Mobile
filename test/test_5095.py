from selenium.webdriver.common.by import By
import time


from pages.texnonews import TexnoNews


def test_texno_news(browser):
    texno_news = TexnoNews(browser)
    texno_news.open()
    texno_news.h1()

















