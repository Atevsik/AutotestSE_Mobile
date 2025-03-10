from selenium.webdriver.common.by import By
import time
from pages.glavnfootball import FootballGlavn


def test_football_fot_glvn(browser):
    fot_glvn = FootballGlavn(browser)
    fot_glvn.open()
    fot_glvn.header()
    fot_glvn.tablo()
    fot_glvn.knopki()
    fot_glvn.top_material()
    fot_glvn.knopka_all_news()
    fot_glvn.video()
    fot_glvn.spisok_reviews(16)
    fot_glvn.knopka_all_reviews()
    fot_glvn.spisok_reviews(26)
    fot_glvn.photo()
    fot_glvn.photo_click()
    fot_glvn.podval()
    fot_glvn.knoka_podval1()
    fot_glvn.knoka_podval2()
    fot_glvn.knoka_podval3()
    fot_glvn.knoka_podval4()
    fot_glvn.knoka_podval5()
    fot_glvn.knoka_podval6()
    fot_glvn.knoka_podval7()
    fot_glvn.knoka_podval8()
