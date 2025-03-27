from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Shev4enko:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/video/den-s-alekseem-shevchenko/materials/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Все материалы')]")

    def knopka(self):
        knopka = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")

    def vid_sport(self):
        vid_sport = self.browser.find_element(By.XPATH,"//div[@class='se-material-filter-menu']")

    def dop_news(self):
        dop_news = self.browser.find_element(By.XPATH,"//a[contains(text(),'Показать еще')]")
        dop_news.click()

    def proverka(self,count):
        proverka = self.browser.find_elements(By.XPATH,"//div[@class='se-news-list-page__item-right']")
        assert len(proverka) == count

    def gazeta(self):
        gazeta = self.browser.find_element(By.XPATH, "//section[@class='se-titled-block mb_20']")










