from selenium.webdriver.common.by import By
import time

from pages.nhl3 import NHL3



def test_nhl3noz(browser):
    nhl3 = NHL3(browser)
    nhl3.open()
    nhl3.header()
    nhl3.tablo()
    nhl3.knopki()
    nhl3.top_material()
    nhl3.knopka_all_news()
    nhl3.podval()
    nhl3.knoka_podval1()
    nhl3.knoka_podval2()
    nhl3.knoka_podval3()
    nhl3.knoka_podval4()
    nhl3.knoka_podval5()
    nhl3.knoka_podval6()
    nhl3.knoka_podval7()
    nhl3.knoka_podval8()










