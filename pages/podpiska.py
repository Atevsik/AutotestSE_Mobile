from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Podpiska:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/company/subscribe/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//span[contains(text(),'Здравствуйте, наш уважаемый читатель!')]")

    def input(self):
        input = self.browser.find_element(By.XPATH,"//input[@name='_member_email']")













