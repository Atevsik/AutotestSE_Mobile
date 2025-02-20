from selenium.webdriver.common.by import By
import time

from pages.prognozi import Prognoz



def test_prognoz(browser):
    prog = Prognoz(browser)
    prog.open()
    prog.header()
    prog.tablo()
    prog.knopki()
    prog.top_material()
    prog.knopka_all_news()
    prog.spisok_reviews(16)
    prog.knopka_all_reviews()
    prog.spisok_reviews(26)
    prog.podpiska()
    prog.podval()
    prog.tur_table()
    prog.akron()
    prog.knoka_podval1()
    prog.knoka_podval2()
    prog.knoka_podval3()
    prog.knoka_podval4()
    prog.knoka_podval5()
    prog.knoka_podval6()
    prog.knoka_podval7()
    prog.knoka_podval8()










