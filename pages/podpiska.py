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

    def knp(self):
        knp = self.browser.find_element(By.XPATH,"//input[@name='bt_save']")
        knp.click()
        assert self.browser.current_url == 'https://sendsay.ru/form/sportexpress/1', "Не правильная подписка"












