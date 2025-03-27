from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class NewsSpiso4:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/news/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Весь спорт.')]")

    def knopka(self):
        knopka = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")

    def knopki1(self):
        knopki1 = self.browser.find_element(By.XPATH,"//a[contains(text(),'Главные')]")
        knopki1.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/news/?isEditorialChoice=1', "Не правильная главная"

    def knopki2(self):
        knopki2 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Выбор читателей')]")
        knopki2.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/news/?isHot=1', "Не правильный выбор читателей"

    def knopki3(self):
        knopki3 = self.browser.find_element(By.XPATH, "//a[@class='se-button se-material-list-filter__button se-material-list-filter__button--exclusive se-button--size-middle']")
        knopki3.click()
        sleep(5)
        assert self.browser.current_url == 'https://m.sport-express.ru/news/?isExclusive=1', "Не правильный эксклюзив"

    def vid_sport(self):
        vid_sport = self.browser.find_element(By.XPATH,"//div[@class='se-material-filter-menu']")

    def dop_news(self):
        dop_news = self.browser.find_element(By.XPATH,"//a[contains(text(),'Показать еще')]")
        dop_news.click()
        sleep(3)

    def proverka(self,count):
        proverka = self.browser.find_elements(By.XPATH,"//div[@class='se-news-list-page__item-right']")
        assert len(proverka) == count

    def k_football(self):
        k_football = self.browser.find_element(By.CSS_SELECTOR,"a[href='/football/news/']")
        k_football.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/football/news/', "Не правильный футбол"

    def selector(self):
        selector = self.browser.find_element(By.XPATH,"//div[@class='se-select__value-container']")
        selector.click()

    def rpl(self):
        rpl = self.browser.find_element(By.XPATH,"//div[3]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]//div[1]//div[3]")
        rpl.click()
        sleep(4)
        assert self.browser.current_url == 'https://m.sport-express.ru/football/rfpl/news/', "Не правильный РПЛ"

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH, "//footer[@class='se-footer']//div[@class='se-center-wrapper']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_159072868052985816']")








