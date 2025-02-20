from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


class Register:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/registration/')
        sleep(5)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[contains(text(),'Быстрая регистрация')]")

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//div[contains(text(),'Регистрация через соцсети')]")

    def pole(self):
        pole = self.browser.find_element(By.XPATH,"//input[@placeholder='Ваш псевдоним']")

    def podval(self):
        podval = self.browser.find_element(By.XPATH,"//footer[@class='se-footer']")
















