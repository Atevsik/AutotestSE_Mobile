from selenium.webdriver.common.by import By
import time
from pages.homepage import HomePage

def test_glavn_se(browser):
    glavn = HomePage(browser)
    glavn.open()
    glavn.knopki_menu()
    glavn.tablo()
    glavn.knopki()
    glavn.top_material()
    #glavn.spisok_news(17)
    glavn.scroll1()
    #glavn.knopka_all_news()
    glavn.video()
    #glavn.spisok_reviews(16)
    #glavn.knopka_all_reviews()
    #glavn.spisok_reviews(26)
    glavn.photo()
    #glavn.scroll2()
    #glavn.photo_click()
    glavn.scroll()
    #glavn.opros_teg(2)
    glavn.podval()
    glavn.knoka_podval1()
    glavn.knoka_podval3()
    glavn.knoka_podval4()
    glavn.knoka_podval5()
    glavn.knoka_podval6()
    glavn.knoka_podval7()
    glavn.knoka_podval8()



