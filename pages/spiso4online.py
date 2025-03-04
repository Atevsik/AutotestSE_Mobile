from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Spiso4Online:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/online/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Видео')]")

    def knopka(self):
        knopka = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")

    def vid_sport(self):
        vid_sport = self.browser.find_element(By.XPATH,"//div[@class='se-material-filter-menu']")

    def dop_news(self):
        dop_news = self.browser.find_element(By.XPATH,"//a[contains(text(),'Показать еще')]")
        dop_news.click()

    def gazeta(self):
        gazeta = self.browser.find_element(By.XPATH, "//section[@class='se-titled-block mb_20']")
        sleep(3)

    def podpiska(self):
        podpiska = self.browser.find_element(By.XPATH,"//div[@class='swiper-slide swiper-slide-active']//a[@class='se-button se-newspaper-widget__button-subscription se-button--size-big'][contains(text(),'Подписка 2025')]")
        podpiska.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/subscribe/', "Не правильная подписка"
        self.browser.back()

    def k_hockey(self):
        k_hockey = self.browser.find_element(By.XPATH,"//a[contains(@class,'se-material-filter-menu__item-button')][contains(text(),'Баскетбол')]")
        k_hockey.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/basketball/online/', "Не правильный БАскет"

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH,"//footer[@class='se-footer']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_159072868052985816']")








