from selenium.webdriver.common.by import By
import time



from pages.texnoreviews import TexnoReviews


def test_texno_news(browser):
    texno_news = TexnoReviews(browser)
    texno_news.open()
    texno_news.h1()


















