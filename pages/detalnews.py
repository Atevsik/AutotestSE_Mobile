from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class DetalNews:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/basketball/vtb-league/news/bratya-kulaginy-voroncevich-lopatin-hill-i-hemmonds-popali-na-match-zvezd-edinoy-ligi-vtb-2024-2174153/')

    def tablo(self):
        tablo = self.browser.find_element(By.XPATH,"//div[@class='se-translation-scoreboard__events']")

    def knopki(self):
        knopki = self.browser.find_element(By.XPATH,"//div[@class='se-translation-scoreboard__buttons-intervals']")

    def autor(self):
        autor = self.browser.find_element(By.XPATH,"//a[contains(text(),'Тимур Ганеев')]")
        autor.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/author/timur-ganeev/', "Не правильный автор"
        self.browser.back()

    def podelit(self):
        podelit = self.browser.find_element(By.XPATH,"//div[@class='se-shareblock__icon']//*[name()='svg']")
        podelit.click()

    def podel_knop(self,count):
        podel_knop = self.browser.find_elements(By.XPATH,"//button[@class='react-share__ShareButton']")
        assert len(podel_knop) == count

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_150116181456951773']")

    def detal_menu(self):
        detal_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")

    def telega_news(self):
        telega_news = self.browser.find_element(By.XPATH,"//div[@class='se-material-page__blog-buttons']")

    def header(self):
        header = self.browser.find_element(By.XPATH,"//div[@class='se-header-mob__inner-stripe']")

    def basket(self):
        basket = self.browser.find_element(By.XPATH,"//span[contains(text(),'Баскетбол')]")
        basket.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/basketball/', "Не правильный баскет"
        self.browser.back()

    def block_next(self):
        block_next = self.browser.find_element(By.XPATH,"//div[@id='material-page-2174153']//div[@class='se-read-also-widget__title'][contains(text(),'Читайте также')]")

    def like(self):
        like = self.browser.find_element(By.XPATH,"//div[@class='se-material-page__footer-socials']")

