from selenium.webdriver.common.by import By
import time

from pages.reviewsspiso4 import ReviewsSpiso4


def test_reviews_spiso4(browser):
    reviews = ReviewsSpiso4(browser)
    reviews.open()
    reviews.h1()
    reviews.knopka()
    reviews.knopki1()
    reviews.knopki2()
    reviews.knopki3()
    reviews.vid_sport()
    reviews.dop_news()
    reviews.gazeta()
    reviews.k_hockey()
    reviews.selector()
    reviews.kxl()
    reviews.scroll()
    reviews.reklama()





