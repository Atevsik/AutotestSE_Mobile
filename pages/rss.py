from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class RSS:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/company/rss/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[@class='se19-staticpage-h1']")

    def basket(self):
        basket = self.browser.find_element(By.XPATH,"//a[contains(text(),'RSS баскетбол')]")
        basket.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/services/materials/news/basketball/se/', "Не правильный рсс"
        self.browser.back()

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//h2[contains(text(),'Телеграм-канал «СЭ»')]")

    def h3(self):
        h3 = self.browser.find_element(By.XPATH, "//h2[contains(text(),'Телеграм-бот «СЭ»')]")

    def h4(self):
        h4 = self.browser.find_element(By.XPATH, "//h2[contains(text(),'Дзен')]")

