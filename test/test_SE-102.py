from selenium.webdriver.common.by import By
import time
from pages.homepage import HomePage

def test_glavn_se(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.tablo_find()
    homepage.plitka()
    homepage.main_news()
    homepage.news()
    homepage.main_video()
    homepage.reviews()
    homepage.photo_main()
    homepage.statblock_main()
    homepage.pollandteg_main(2)
    homepage.reklama_baner()




