from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Politika:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/company/usematerial/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Правовая информация')]")

    def text(self):
        text = self.browser.find_element(By.XPATH,"//h3[contains(text(),'Использование Сайта')]")









