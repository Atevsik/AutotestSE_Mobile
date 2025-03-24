from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Spiso4Story:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/stories/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Весь спорт.')]")

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

    def k_hockey(self):
        k_hockey = self.browser.find_element(By.XPATH,"//a[contains(@class,'se-material-filter-menu__item-button')][contains(text(),'Фигурное катание')]")
        k_hockey.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/figure-skating/stories/', "Не правильный фигурка"

    def selector(self):
        selector = self.browser.find_element(By.XPATH,"//div[@class='se-select__value-container']")
        selector.click()

    def mma(self):
        mma = self.browser.find_element(By.XPATH,"//div[@class='se-select__item'][contains(text(),'Чемпионат Европы')]")
        mma.click()
        sleep(4)
        assert self.browser.current_url == 'https://m.sport-express.ru/figure-skating/chempionat-evropy/stories/', "Не правильный ЧЕ"

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH, "//div[@class='swiper-slide swiper-slide-active']//a[@class='se-button se-newspaper-widget__button-subscription se-button--size-big'][contains(text(),'Подписка 2025')]")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_159072868052985816']")








