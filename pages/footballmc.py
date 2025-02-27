from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class FootballMc:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/live/football/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_150116227789998723']")

    def book(self):
        book = self.browser.find_element(By.XPATH,"//div[@class='se-matchcenter-sports-list__extra']")















