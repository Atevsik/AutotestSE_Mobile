from selenium.webdriver.common.by import By
import time


from pages.figyrkamaterials import FigyrkaNews


def test_mma_figyrka_news(browser):
    fig_news = FigyrkaNews(browser)
    fig_news.open()
    fig_news.h1()
    fig_news.dop_menu()
    fig_news.obsh()
    fig_news.knp1()












