
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

class TexnoNews:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/cybersport/news/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Техно. Новости')]")









