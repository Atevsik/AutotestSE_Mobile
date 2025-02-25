from selenium.webdriver.common.by import By
import time
from pages.dayshev4enko import Shev4enko


def test_day(browser):
    day = Shev4enko(browser)
    day.open()
    day.h1()
    day.knopka()
    day.vid_sport()
    day.gazeta()
    day.proverka(10)
    day.dop_news()







