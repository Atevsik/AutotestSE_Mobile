
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

class Basketeuro:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/basketball/euroleague/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Евролига')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[contains(text(),'Женщины')]")
        obsh.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/basketball/L/women/euroleague/2024-2025/', "No reviews"

















