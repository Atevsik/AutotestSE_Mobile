from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class DetalReviews:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/hockey/nhl/reviews/biografiya-ueyna-gretcki-zhizn-i-sportivnaya-karera-legendarnogo-kanadskogo-hokkeista-i-trenera-2174095/')
        sleep(6)
        sleep(3)

    def tablo(self):
        tablo = self.browser.find_element(By.XPATH,"//div[@class='se-translation-scoreboard__events']")

    def knopki(self):
        knopki = self.browser.find_element(By.XPATH,"//div[@class='se-translation-scoreboard__buttons-intervals']")

    def autor(self):
        autor = self.browser.find_element(By.XPATH,"//a[contains(text(),'Анастасия Рацкевич')]")
        autor.click()
        sleep(4)
        assert self.browser.current_url == 'https://m.sport-express.ru/author/anastasia-ratzkevitch/', "Не правильный автор"
        self.browser.back()

    def podelit(self):
        podelit = self.browser.find_element(By.XPATH,"//div[@class='se-shareblock__icon']//*[name()='svg']")
        podelit.click()
        sleep(4)

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
        basket = self.browser.find_element(By.XPATH,"//span[contains(text(),'Уэйн Гретцки')]")
        basket.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/ueyn-gretcki-2722/', "Не правильный teg"
        self.browser.back()

    def like(self):
        like = self.browser.find_element(By.XPATH,"//div[@class='se-material-page__footer-socials']")

    def soderj_reklama(self):
        soderj_reklama = self.browser.find_element(By.XPATH,"//div[@id='se_toc']")

    def proverka(self):
        proverka = self.browser.find_element(By.XPATH,"//div[@class='table-of-contents__title']")



