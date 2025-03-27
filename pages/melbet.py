from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Melbet:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/football/rus_d1/news/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Мелбет Первая Лига России по футболу - новости')]")

    def knopki1(self):
        knopki1 = self.browser.find_element(By.XPATH,"//a[contains(text(),'Главные')]")
        knopki1.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/football/rus_d1/news/?isEditorialChoice=1', "Не правильная главная"

    def knopki2(self):
        knopki2 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Выбор читателей')]")
        knopki2.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/football/rus_d1/news/?isHot=1', "Не правильный выбор читателей"

    def knopki3(self):
        knopki3 = self.browser.find_element(By.XPATH, "//a[@class='se-button se-material-list-filter__button se-material-list-filter__button--exclusive se-button--size-middle']")
        knopki3.click()
        sleep(5)
        assert self.browser.current_url == 'https://m.sport-express.ru/football/rus_d1/news/?isExclusive=1', "Не правильный эксклюзив"

    def vid_sport(self):
        vid_sport = self.browser.find_element(By.XPATH,"//div[@class='se-material-filter-menu']")

    def material(self,count):
        material = self.browser.find_elements(By.XPATH,"//div[@class='se-news-list-page__item-right']")
        assert len(material) == count





