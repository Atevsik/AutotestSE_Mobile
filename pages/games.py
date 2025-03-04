from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

class Games:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/games/')
        sleep(6)
        sleep(5)

    def logo(self):
        logo = self.browser.find_element(By.XPATH,"//img[@src='//ss.sport-express.ru/fb/modules/gamecenter/img/logo.svg']")

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[contains(text(),'Квизы')]")

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//div[contains(text(),'Тесты')]")