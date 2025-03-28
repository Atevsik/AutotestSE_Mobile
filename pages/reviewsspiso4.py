from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class ReviewsSpiso4:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/reviews/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Весь спорт.')]")

    def knopka(self):
        knopka = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")

    def knopki1(self):
        knopki1 = self.browser.find_element(By.XPATH,"//a[contains(text(),'Главные')]")
        knopki1.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/reviews/?isEditorialChoice=1', "Не правильная главная"

    def knopki2(self):
        knopki2 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Выбор читателей')]")
        knopki2.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/reviews/?isHot=1', "Не правильный выбор читателей"

    def knopki3(self):
        knopki3 = self.browser.find_element(By.XPATH, "//a[@class='se-button se-material-list-filter__button se-material-list-filter__button--exclusive se-button--size-middle']")
        knopki3.click()
        sleep(5)
        assert self.browser.current_url == 'https://m.sport-express.ru/reviews/?isExclusive=1', "Не правильный эксклюзив"

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
        k_hockey = self.browser.find_element(By.XPATH,"//a[contains(@class,'se-material-filter-menu__item-button')][contains(text(),'Хоккей')]")
        k_hockey.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/reviews/', "Не правильный хоккей]"

    def selector(self):
        selector = self.browser.find_element(By.XPATH,"//div[@class='se-select__value-container']")
        selector.click()

    def kxl(self):
        kxl = self.browser.find_element(By.XPATH,"//div[@class='se-select__items']//div[2]")
        kxl.click()
        sleep(4)
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/khl/reviews/', "Не правильный КХЛ"

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH, "//div[@class='swiper-slide swiper-slide-active']//a[@class='se-button se-newspaper-widget__button-subscription se-button--size-big'][contains(text(),'Подписка 2025')]")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_159072868052985816']")








