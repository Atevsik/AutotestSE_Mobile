from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class NewsSpiso4:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/')

