from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Priloj:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/projects/apps/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h2[contains(text(),'Официальное мобильное приложение «Спорт-Экспресс» ')]")

    def knp(self):
        knp = self.browser.find_element(By.XPATH,"//div[@class='apps-links__row']")

    def podval(self):
        podval = self.browser.find_element(By.XPATH,"//footer[@class='se-footer']")












