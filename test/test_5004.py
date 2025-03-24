from selenium.webdriver.common.by import By
import time

from pages.detalreviews import DetalReviews


def test_detal_reviews(browser):
    detal_reviews = DetalReviews(browser)
    detal_reviews.open()
    detal_reviews.tablo()
    detal_reviews.knopki()
    #detal_reviews.autor()  -- Банер добавить закрывашку
    detal_reviews.podelit()
    detal_reviews.podel_knop(5)
    detal_reviews.reklama()
    detal_reviews.detal_menu()
    detal_reviews.telega_news()
    detal_reviews.header()
    #detal_reviews.basket() -- Банер добавить закрывашку
    detal_reviews.like()
    detal_reviews.soderj_reklama()
    detal_reviews.proverka()








