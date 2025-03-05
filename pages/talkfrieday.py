from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Talk:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/fridays/materials/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Все материалы')]")

    def knopka(self):
        knopka = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")

    def knopki1(self):
        knopki1 = self.browser.find_element(By.XPATH,"//a[contains(text(),'Главные')]")
        knopki1.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/fridays/materials/?isEditorialChoice=1', "Не правильная главная"

    def knopki2(self):
        knopki2 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Выбор читателей')]")
        knopki2.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/fridays/materials/?isHot=1', "Не правильный выбор читателей"

    def knopki3(self):
        knopki3 = self.browser.find_element(By.XPATH, "//a[@class='se-button se-material-list-filter__button se-material-list-filter__button--exclusive se-button--size-middle']")
        knopki3.click()
        sleep(5)
        assert self.browser.current_url == 'https://m.sport-express.ru/fridays/materials/?isExclusive=1', "Не правильный эксклюзив"

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









