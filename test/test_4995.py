from selenium.webdriver.common.by import By
import time
from pages.spiso4news import NewsSpiso4


def test_news_spiso4(browser):
    news = NewsSpiso4(browser)

