from selenium.webdriver.common.by import By
import time

from pages.lijinews import LijiNews


def test_lij_news(browser):
    lij_news = LijiNews(browser)
    lij_news.open()
    lij_news.h1()
    lij_news.dop_menu()
    lij_news.obsh()














