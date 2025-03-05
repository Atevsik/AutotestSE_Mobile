from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Contakt:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/company/contacts/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Контактная информация')]")

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//div[contains(text(),'Партийный переулок.1, корпус 57, строение 1, этаж ')]")

    def h3(self):
        h3 = self.browser.find_element(By.XPATH,"//div[normalize-space()='+7 (495) 540-70-10']")

    def h4(self):
        h4 = self.browser.find_element(By.XPATH,"//a[normalize-space()='feedback@sport-express.ru']")










