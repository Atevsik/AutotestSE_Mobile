from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class MMAraiting:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/fighting/mma/ufc/2024/ratings/men/')

    def dopmenu(self):
        dopmenu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")

    def header(self):
        header = self.browser.find_element(By.XPATH,"//div[@class='se-header-mob__inner-stripe']")

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'UFC. Календарь')]")

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def h3(self):
        h3 = self.browser.find_element(By.XPATH,"//div[@class='se-competition-titled-block__title']")

    def boets(self):
        boets = self.browser.find_element(By.XPATH,"//a[contains(text(),'Тацуро Тайра')]")
        boets.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/tacuro-tayra-26076/', "Не правильный боец"
        self.browser.back()

    def champion(self):
        champion = self.browser.find_element(By.XPATH,"//div[@class='se-fighter-champion-panel se-fighter-champion-panel--champion-mma']")

    def selector(self):
        selector = self.browser.find_element(By.XPATH,"//div[@class='se-select__value-container'][contains(text(),'Наилегчайший вес')]")
        selector.click()

    def ves(self):
        ves = self.browser.find_element(By.XPATH,"//div[@class='se-page-filter sp-ratings-filter__item']//div[@class='se-select__items']//div[2]")
        ves.click()

    def jen(self):
        jen = self.browser.find_element(By.XPATH,"//div[@class='se-buttons-toggle-item']")
        jen.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/fighting/mma/ufc/2024/ratings/women/', "Не правилный вумен"

    def vala(self):
        vala = self.browser.find_element(By.XPATH,"//a[contains(text(),'Валентина Шевченко')]")
        vala.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/valentina-shevchenko-mma-25327/', "Не правильная валя "


