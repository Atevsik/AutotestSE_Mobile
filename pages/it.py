from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class IT:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/company/it/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'IT деятельность')]")

    def text(self):
        text = self.browser.find_element(By.XPATH,"//p[contains(text(),'Акционерное общество «СПОРТ-ЭКСПРЕСС» (ОГРН 102773')]")


















